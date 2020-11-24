from django import template

register = template.Library()


# Return movie/tv to iterate over
@register.simple_tag
def get_obj(row):
    x = getattr(row, 'movie', None)
    if x is None:
        x = getattr(row, 'tv', None)
    return x


@register.simple_tag
def get_random_url(item):
    from movie.models import Movie
    import random
    # is_soap = random.randint(0, 1)
    is_soap = 1

    url = ''
    # if item:
    # if getattr(item, 'title', None):
    if 'title' in item:
        url += '/movie/'
        if bool(is_soap):
            # url += str(item.pk)
            url += str(item['id'])
        else:
            url += str(item.title)
    else:
        url += '/tv/'
        if bool(is_soap):
            # url += str(item.pk)
            url += str(item['id'])
        else:
            url += str(item.name)

    return url








