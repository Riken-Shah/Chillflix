from django.contrib import admin
from tv.models import Show, NextEpisodeToAir, LastEpisodeToAir

admin.site.register(Show)
admin.site.register(NextEpisodeToAir)
admin.site.register(LastEpisodeToAir)
