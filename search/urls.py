from django.urls import path
from .views import search_api, Search, filter_api
urlpatterns = [
    path('', Search.as_view()),
    path('api/search', search_api),
    path('api', search_api),
    path('api/search/filter', filter_api)
]
