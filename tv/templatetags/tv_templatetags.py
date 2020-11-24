from django import template
from TMDB.real_tmdb import TMDB
from django.template.defaultfilters import truncatewords
from TMDB.upload_helper import UploadTMDB

register = template.Library()
tmdb = TMDB()


# Get TV Credits
@register.simple_tag
def get_tv_credits(tmdb_id):
    return tmdb.tmdb.TV(tmdb_id).credits()


# Get tv certification
@register.simple_tag
def get_certification_tv(tmdb_id):
    return tmdb.tmdb.TV(tmdb_id).content_ratings()


# Get similar tv
@register.simple_tag
def get_similar_tv(tmdb_id):
    x = tmdb.tmdb.TV(tmdb_id).similar()
    return UploadTMDB().check_shows_list_from_our_db(x['results'])


# Get the valid seasons
@register.simple_tag
def get_all_season(seasons: list):
    if type(seasons) is list:
        for s in seasons:
            if s['name'] == 'Specials':
                seasons.remove(s)
                return seasons
    else:
        for s in seasons.all():
            if s.name == 'Specials':
                seasons.remove(s)
                return seasons
    return seasons


# Get episodes info
@register.simple_tag
def get_episodes(tmdb_id, season_no):
    return tmdb.tmdb.TV_Seasons(tmdb_id, season_no).info()


@register.simple_tag
def set(val):
    return val


# Truncate chars
@register.simple_tag
def turnc_text(text, max_chars: int):
    if len(text) > max_chars:
        resp = {'first': text[:max_chars] + '…', 'last': text[max_chars:]}
        return resp
    return {'first': text}


@register.simple_tag
def turnc_word(text, max_word: int):
    resp = {'first': truncatewords(text, max_word)}
    if resp['first'].find('…') != -1:
        resp['last'] = text[len(resp['first']) - 1:]
    return resp


@register.simple_tag
def get_certification_tv(releases):
    # If country=None It will return any certification ;)
    def check_for_country(li, country=None):
        for i in li:
            if country is not None:
                if i['iso_3166_1'] == country and i['rating'] != '':
                    return i
            else:
                if i['rating'] != '':
                    return i
        return False

    # Checking for IN first
    releases = releases['results']
    i = check_for_country(releases, 'IN')
    # Checking for US
    if not i:
        i = check_for_country(releases, 'US')
        if not i:
            i = check_for_country(releases)
            if not i:
                return None
            else:
                return i
        else:
            return i
    else:
        return i
    return None


@register.filter
def assign(arg, value):
    arg = value
    return arg
