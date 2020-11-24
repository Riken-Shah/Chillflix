from django.shortcuts import render, redirect
# from TMDB.pure_tmdb import RealTMDb
from django.views.generic.list import ListView
# import tmdbsimple
# import time
# from data_api.my_tmdb import Search as SEARCH
from chillflix.settings import real_tmdb
from pprint import pprint


# Returns a search text
def search(query, page=1):
    return real_tmdb.tmdb.Search().multi(query=query, region='IN', page=page)
    # return {'results': [], 'total_pages': 100}


# This function will resolve search query
def resolve_search(data):
    if not data['query']:
        return False
    return search(data['query'], page=data['page']) or False


# This will resolve filter search
def resolve_filter_search(data):
    type_ = data['type']
    if not type_:
        return False

    # Unwanted items
    unwanted_general_items = ['type', 'csrfmiddlewaretoken', 'certification']
    # UNCOMMON TV LIST ITEMS
    tv_items = ['first_air_date_gte', 'first_air_date_lte', ]
    # UNCOMMON MOVIE LIST ITEMS
    movie_items = ['primary_release_date_gte', 'primary_release_date_lte', ]

    new_data = {}

    # Cleaning data if movie
    if type_ == 'movie':
        # Getting instance for movie or type
        instance = getattr(real_tmdb.tmdb.Discover(), type_)

        print('From resolve filter search...')
        pprint({k: v for (k, v) in data.items() if k not in unwanted_general_items + tv_items})

        # Creating new dict from data to remove unwanted items
        new_data = {k: v for (k, v) in data.items() if k not in unwanted_general_items + tv_items}

        # Cleaning data
        new_data['primary_release_date_gte'] = f"{data['primary_release_date_gte']}-01-01"
        new_data['primary_release_date_lte'] = f"{data['primary_release_date_lte']}-12-31"

        return instance(**new_data) or False


#  Search Class
class Search(ListView):
    template_name = 'search/home_tv.html'
    context_object_name = 'page'
    paginate_by = 1
    data = {'page': -1}

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', 'None')
        page = self.request.GET.get('page', 1)
        pprint('Getting context data...')
        # If data already exist
        if self.data['page'] == page:
            row = self.data['row']
        else:
            # Getting Data
            row = search(query, page)
        data['row'] = row
        return data

    def get_queryset(self, *args, **kwargs):
        self.extra_context = self.request.GET
        self.request.GET._mutable = True
        page = self.request.GET.get('page', 1)
        if self.request.GET.get('discover', None):
            self.data['row'] = resolve_filter_search(self.request.GET)
            # type_ = self.request.GET.get('type')
            # del self.request.GET['type']
            # del self.request.GET['discover']
            # from operator import itemgetter
            # raw_data = dict(filter(itemgetter(1), self.request.GET.items()))
            # raw_data['primary_release_date_gte'] = f"{raw_data['primary_release_date_gte']}-01-01"
            # raw_data['primary_release_date_lte'] = f"{raw_data['primary_release_date_lte']}-12-31"
            # raw_data['first_air_date_gte'] = f"{raw_data['first_air_date_gte']}-01-01"
            # raw_data['first_air_date_lte'] = f"{raw_data['first_air_date_lte']}-12-31"
            # if type_ == 'movie':
            #     del raw_data['first_air_date_gte']
            #     del raw_data['first_air_date_lte']
            # else:
            #     del raw_data['primary_release_date_gte']
            #     del raw_data['primary_release_date_lte']
            #
            # pprint(raw_data)
            # instance = getattr(real_tmdb.tmdb.Discover(), type_)
            # # self.data = {'page': page, 'row': instance(**raw_data, page=page)}
            # self.data = {'page': 1, 'row': []}
            # self.extra_context['discover'] = True
            # self.extra_context['type'] = type_
        else:
            query = self.request.GET.get('query', 'Dil')
            query = 'Dil' if query == '' else query
            self.data = {'page': page, 'row': search(query, page)}

        print(f'QPage -> ', page)
        print('For queryset')
        row = [i for i in range(int(self.data['row']["total_pages"]))]
        return row


# Create your views here.
def search_api(request):
    if request.method == 'POST':
        page = request.POST.get('page', 1)
        for_ = request.POST.get('for', None)

        if request.POST.get('discover', None):
            request.POST._mutable = True

            type_ = request.POST.get('type')
            del request.POST['type']
            del request.POST['csrfmiddlewaretoken']
            del request.POST['discover']
            del request.POST['for']
            from operator import itemgetter
            raw_data = dict(filter(itemgetter(1), request.POST.items()))
            raw_data['primary_release_date_gte'] = f"{raw_data['primary_release_date_gte']}-01-01"
            raw_data['primary_release_date_lte'] = f"{raw_data['primary_release_date_lte']}-12-31"
            pprint(raw_data)
            instance = getattr(real_tmdb.tmdb.Discover(), type_)
            resp = instance(**raw_data)['results']
        else:
            print('QUERY')
            query = request.POST.get('query', 'Dil')
            query = 'Dil' if query == '' else query
            resp = search(query, page)
    else:
        return redirect('home')
    print(f'\n\n\n{page}\n\n\n')
    if for_:
        print('HERE')
        temp = 'search/in_item.html'
    else:
        print('HERE BRO', query)
        temp = 'home/search_results.html'

    return render(request, temp, {"row": resp})


def filter_api(request):
    row = None
    if request.POST:
        row = resolve_filter_search(request.POST)

    pprint(row)
    return render(request, 'search/in_item.html', {'row': row})

