from TMDB.pure_tmdb import RealTMDb
from home.models import Genres


class GenreBox():
    def __init__(self):
        self.tmdb = RealTMDb().tmdb
        self.img_path = 'backdrop_path'

    def update_movie_genres(self):
        movie_genres = self.tmdb.Genres().movie_list()['genres']
        discover = self.tmdb.Discover()
        for genre in movie_genres:
            genre['type'] = 'movie'
            genre_movies = discover.movie(with_genres=f'{genre["id"]}')['results']
            poster_path = None
            for movie in genre_movies:
                if self.img_path in movie:
                    poster_path = movie[self.img_path]
                    break
            genre[self.img_path] = poster_path
            Genres.objects.update_or_create(defaults=genre, id=genre['id'])

    def update_tv_genres(self):
        tv_genres = self.tmdb.Genres().tv_list()['genres']
        discover = self.tmdb.Discover()
        for genre in tv_genres:
            genre['type'] = 'tv'
            genre_shows = discover.tv(with_genres=f'{genre["id"]}')['results']
            poster_path = None
            for tv in genre_shows:
                if self.img_path in tv:
                    poster_path = tv[self.img_path]
                    break
            genre[self.img_path] = poster_path
            Genres.objects.update_or_create(defaults=genre, id=genre['id'])

    def update_all(self):
        self.update_movie_genres()
        self.update_tv_genres()


if __name__ == '__main__':
    g = GenreBox()
    g.update_all()