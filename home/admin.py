from django.contrib import admin
from .models import MovieList, ShowList, Genres

admin.site.register(MovieList)
admin.site.register(ShowList)
admin.site.register(Genres)
