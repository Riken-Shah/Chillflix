from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from .models import Movie
from django_user_agents.utils import get_user_agent
import tmdbsimple
from home.models import MovieList
from random import shuffle
from chillflix.settings import real_tmdb


class Home(ListView):
    template_name = 'home/home_tv.html'
    template_mobile = 'home/home_mobile.html'
    template_tablet = 'home/home_tablet.html'
    tmdb = real_tmdb
    # queryset = tmdb.get_rows_from_db()
    qs = list(MovieList.objects.all())
    shuffle(qs)
    queryset = qs
    context_object_name = 'rows'
    paginate_by = 2
    c = list(Movie.objects.all())
    c.sort(key=lambda x: x.popularity)
    carousel = c[:10]
    extra_context = {'carousel': carousel}

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            self.template_name = self.template_mobile
        elif user_agent.is_tablet:
            self.template_name = self.template_tablet

        return super(Home, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tmdb = tmdbsimple
        discover = tmdb.Discover()
        for i in data['rows']:
            # This will execute code that will get us data
            exec(i.code)
        return data


class PLAY(View):
    template_name = 'movie/movie_details.html'
    template_mobile = 'movie/play_mobile.html'
    template_tablet = 'movie/stream_tablet.html'

    def get(self, requests, tmdb_id):
        user_agent = get_user_agent(requests)
        item = tmdbsimple.Movies(tmdb_id).info(append_to_response='credits,similar,releases')
        if user_agent.is_mobile:
            return render(requests, self.template_mobile, context={'item': item, 'type': 'movie'})
        elif user_agent.is_tablet:
            return render(requests, self.template_tablet, context={'item': item, 'type': 'movie'})
        else:
            return render(requests, self.template_name, context={'item': item, 'type': 'movie'})


