import django
import os

def initial_setup():
    # Uploading Carousel Movie and Shows
    TMDB().upload_carousel_items()
    # Uploading Type of Movie ans Show Rows
    MovieLists().update_all()
    AllShowList().update_all()
    # Uploading Genres For Filter
    GenreBox().update_all()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chillflix.settings")
    django.setup()
    from TMDB.real_tmdb import TMDB
    from TMDB.MovieList import MovieLists
    from TMDB.ShowList import AllShowList
    from TMDB.Genres import GenreBox
    # Setting up the initial data
    initial_setup()
