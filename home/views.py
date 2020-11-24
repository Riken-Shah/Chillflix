from random import shuffle
from django.views.generic.list import ListView
from tv.models import Show
from home.models import ShowList, MovieList
from movie.models import Movie
from django_user_agents.utils import get_user_agent
from chillflix.settings import real_tmdb


class Home(ListView):
    tmdb = real_tmdb.tmdb
    qs = list(MovieList.objects.all().union(ShowList.objects.all()))
    shuffle(qs)
    queryset = qs
    template_name = 'home/home_tv.html'
    template_mobile = 'home/home_mobile.html'
    template_tablet = 'home/home_tablet.html'
    context_object_name = 'rows'
    paginate_by = 1
    c = list(Movie.objects.all()) + list(Show.objects.all())
    # c = Movie.objects.all().union(Show.objects.all())
    c.sort(key=lambda x: x.popularity)
    carousel = c[:10]
    extra_context = {'carousel': carousel}

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            self.template_name = self.template_mobile
            self.extra_context['is_tablet'] = False
        elif user_agent.is_tablet and not user_agent.is_pc:
            self.template_name = self.template_tablet
            self.extra_context['is_tablet'] = True
        else:
            self.extra_context['is_tablet'] = False
        return super(Home, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tmdb = real_tmdb.tmdb
        discover = tmdb.Discover()
        for i in data['rows']:
            # This will execute code that will get us data
            # print(f'i.code => {i.code}')
            exec(i.code)
        return data





