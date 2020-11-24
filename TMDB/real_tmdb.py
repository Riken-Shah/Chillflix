import tmdbsimple
from TMDB.upload_helper import UploadTMDB
from movie.models import Movie
from tv.models import Show
import environ

env = environ.Env()


class TMDB:
    API_KEY = env('TMDB_API_KEY')

    def __init__(self):
        self.tmdb = tmdbsimple
        self.tmdb.API_KEY = self.API_KEY
        self.helper = UploadTMDB()

    def add_videos_movie(self, movie):
        m = []
        for i in movie:
            x = self.tmdb.Movies(id=i['id']).info(append_to_response='videos')
            x['videos'] = x['videos']['results']
            m.append(x)

        return m

    def add_videos_tv(self, tv):
        m = []
        for i in tv:
            x = self.tmdb.TV(id=i['id']).info(append_to_response='videos')
            x['videos'] = x['videos']['results']
            m.append(x)

        return m

    # Upload Carousel Item in Our Local DB
    def upload_carousel_items(self):

        movies = self.add_videos_movie(self.tmdb.Movies().popular()['results'])
        shows = self.add_videos_tv(self.tmdb.TV().popular()['results'])

        Movie.objects.all().delete()
        Show.objects.all().delete()

        for movie in movies:
            self.helper.upload_movie_to_local_db(movie)
            print(f'Movie {movie["title"]} added')

        for show in shows:
            self.helper.upload_tv_to_local_db(show)
            print(f'TV {show["name"]} added')


if __name__ == '__main__':
    c = TMDB()
    c.upload_carousel_items()
