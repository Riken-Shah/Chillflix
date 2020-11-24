from django.urls import path, re_path
from .views import Home, PLAY
urlpatterns = [
    path('', Home.as_view()),
    re_path(r'^(?P<tmdb_id>[0-9]+)$', PLAY.as_view()),
]
