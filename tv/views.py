from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Show
from django_user_agents.utils import get_user_agent
from django.views import View
import tmdbsimple
from TMDB.pure_tmdb import RealTMDb
from home.models import ShowList


class Home(ListView):
    from random import shuffle
    template_name = 'home/home_tv.html'
    template_mobile = 'home/home_mobile.html'
    template_tablet = 'home/home_tablet.html'
    tmdb = RealTMDb()
    # queryset = tmdb.get_rows_from_db()
    qs = list(ShowList.objects.all())
    shuffle(qs)
    queryset = qs
    context_object_name = 'rows'
    paginate_by = 2
    c = list(Show.objects.all())
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
    template_mobile = 'tv/play_mobile.html'
    template_tablet = 'movie/stream_tablet.html'

    def get(self, requests, tmdb_id, season_number):
        user_agent = get_user_agent(requests)
        item = tmdbsimple.TV(tmdb_id).info(append_to_response='credits,similar,content_ratings')
        if not season_number:
            season_number = 1
        if user_agent.is_mobile:
            return render(requests, self.template_mobile, context={'item': item, 'type': 'tv', 'main_season': season_number})
        elif user_agent.is_tablet:
            return render(requests, self.template_tablet, context={'item': item, 'type': 'tv', 'main_season': season_number})
        else:
            return render(requests, self.template_name, context={'item': item, 'type': 'tv', 'main_season': season_number})

