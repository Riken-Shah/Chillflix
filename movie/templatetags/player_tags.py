from django import template
from TMDB.pure_tmdb import RealTMDb
from django.template.defaultfilters import truncatewords
from TMDB.upload_helper import UploadTMDB
import requests
import json
register = template.Library()


# Resolve Rating (5 Star)
@register.simple_tag
def resolve_rating(value):
    value = round(value / 2)
    checked = []
    for i in range(5):
        if i < value:
            # checked add color
            checked.append('checked')
        else:
            checked.append('')
    return checked


# Fix the overview length problem
@register.simple_tag
def fix_overview(overview, words):
    if not overview:
        return None
    overview_truncate = truncatewords(overview, words)
    add_more_info = False
    if overview_truncate[-1] == '…':
        add_more_info = True
        reaming_text = overview[len(overview_truncate) - 1:]
        return {'overview': overview_truncate[:-1], 'add_info': add_more_info, 'reaming_text': reaming_text}
    return {'overview': overview_truncate, 'add_info': add_more_info}


# Convert int minute to -> hr min format
@register.simple_tag
def get_hr_min_format(minute):
    if not minute:
        return None
    elif type(minute) == list:
        minute = minute[0]

    k = '{:2d} hr {:2d} min'.format(*divmod(int(minute), 60))
    k = k.replace('00 hr', '')
    k = k.replace('00 min', '')
    k = k.replace('0 hr', '')
    k = k.replace('0 min', '')
    k = k.replace('0min', '')
    k = k.replace('0hr', '')

    return k


# Get Movie Credits
@register.simple_tag
def get_movie_credits(tmdb_id):
    tmdb = RealTMDb()
    return tmdb.tmdb.Movies(tmdb_id).credits()


@register.simple_tag
def get_similar_movies(tmdb_id):
    tmdb = RealTMDb()
    return UploadTMDB().check_movies_list_from_our_db(tmdb.tmdb.Movies(tmdb_id).similar_movies()['results'])


# Get Director from Credits.
@register.simple_tag
def get_director(crew, max_=None):
    directors = []
    for people in crew:
        if people['job'] == 'Director':
            directors.append(people)
    return directors[:max_]


@register.simple_tag
def date_fix(mydate):
    if not mydate:
        return None
    from datetime import datetime
    date_ = datetime.strptime(mydate, '%Y-%m-%d').date()
    month = date_.strftime('%B')[:3]
    return month + date_.strftime(' %d, %Y')


@register.simple_tag
def get_certification_movie(releases: dict):
    def check_for_country(li, country=None):
        for i in li:
            if country is not None:
                if i['iso_3166_1'] == country and i['certification'] != '':
                    # return i['iso_3166_1'], i['certification']
                    return i
            else:
                if i['certification'] != '':
                    # return i['iso_3166_1'], i['certification']
                    return i

        return False

    if 'countries' in releases:
        li = releases['countries']
        country = None
        certification = None
        # Checking for IN first
        i = check_for_country(li, 'IN')
        # Checking for US
        if not i:
            i = check_for_country(li, 'US')
            if not i:
                i = check_for_country(li)
                if not i:
                    return None
                else:
                    return i
            else:
                return i
        else:
            return i

    return None, None


@register.filter
def date_fix(date):
    if date:
        return date[:4]
    return None


@register.simple_tag
def crew_tuple(crew: dict, max_size=10):
    tuple_crew = []
    included = []
    crew = crew
    for member in crew:
        for another in crew:
            if member['name'] not in included:
                if member['name'] == another['name']:
                    print(member['job'], another['job'])
                    member['job'] += f', {another["job"]}'
                    tuple_crew.append(member)
                else:
                    tuple_crew.append(member)
                included.append(member['name'])
    main_fields = ['Director']
    for i in tuple_crew:
        if i['job'].find('Director') - 1:
            temp = tuple_crew[0]
            tuple_crew[0] = i
            tuple_crew[tuple_crew.index(i)] = temp

    return tuple_crew


@register.simple_tag
def get_main_crew(crew, max_=None):
    directors = []
    for people in crew:
        if people['job'] == 'Director':
            directors.append(people)
    return directors[:max_]


@register.filter
def get_trailer_link(videos):
    for video in videos:
        # print(video.site)
        if video.type == 'Trailer' and video.site == 'YouTube':
            return video.key


@register.filter
def get_type(item):
    if type(item) is dict:
        if 'name' in item:
            return 'tv'
        elif 'title' in item:
            return 'movie'
    else:
        if hasattr(item, 'name'):
            return 'tv'
        else:
            return 'movie'


from itertools import zip_longest


@register.filter
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


@register.filter
def _next(item):
    return next(item)

@register.filter
def subtract(value, arg):
    return value - arg

from chillflix.settings import real_tmdb
from home.models import Genres


@register.simple_tag
def get_all_genres():
    movie_obj = list(Genres.objects.filter(type='movie'))
    tv_obj = list(Genres.objects.filter(type='tv'))
    return movie_obj[:4] + tv_obj[:4] + movie_obj[5:] + tv_obj[5:]


@register.simple_tag
def get_all_country():
    return real_tmdb.tmdb.Configuration().countries()


@register.simple_tag
def get_all_languages():
    return real_tmdb.tmdb.Configuration().languages()


@register.filter
def to_js_dict(obj):
    return json.dumps(obj)
