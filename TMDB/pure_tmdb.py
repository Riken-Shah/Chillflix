import tmdbsimple
from TMDB.upload_helper import UploadTMDB
import environ

env = environ.Env()


class RealTMDb:
    API_KEY = env('TMDB_API_KEY', None)

    def __init__(self):
        self.tmdb = tmdbsimple
        self.tmdb.API_KEY = self.API_KEY
        self.upload_tmdb = UploadTMDB()

    # Add Extra Movie Details: certification, videos
    def xtra_movie_details(self, tmdb_id):
        xtra_movie = {}
        xtra_movie['certification_country'], xtra_movie['certification'] = self.upload_tmdb.get_movie_certification(
            tmdb_id)
        return xtra_movie

    # Add Extra TV Details
    def xtra_show_details(self, tmdb_id):
        xtra_show = {}
        xtra_show['iso_3166_1'], xtra_show['rating'] = self.upload_tmdb.get_show_certification(
            tmdb_id)
        return xtra_show

    # Get Carousel Details
    def movie_carousel_details(self):
        movies = self.tmdb.Movies().popular()['results']
        shows = self.tmdb.TV().popular()['results']
        return movies, shows

    def update_carousel(self):
        movies, shows = self.movie_carousel_details()
        for movie in movies:
            tmdb_id = movie['id']
            movie = self.tmdb.Movies(tmdb_id).info(append_to_response='videos')
            movie['videos'] = movie['videos']['results']
            movie.update(self.xtra_movie_details(tmdb_id))
            # movie_inst = self.upload_tmdb.upload_movie_to_local_db(movie)
            # Carousel.movie.add(movie)

        for show in shows:
            tmdb_id = show['id']
            show = self.tmdb.TV(tmdb_id).info(append_to_response='videos')
            show['videos'] = show['videos']['results']
            show.update(self.xtra_show_details(tmdb_id))


if __name__ == '__main__':
    a = RealTMDb()
    a.update_carousel()
