from TMDB.pure_tmdb import RealTMDb
from home.models import MovieList


class MovieLists(RealTMDb):
    resp = []

    def __init__(self):
        super().__init__()

    def add_to_resp(self, item):
        self.resp.append(item)

    def make_list(self, name, code):
        item = {'name': name, 'code': f'i.items = {code}["results"]'}
        self.add_to_resp(item)
        return item

    def upload_all_genres(self):
        movie_list = self.tmdb.Genres().movie_list()['genres']
        base_name = 'Movies Popular in '
        for genre in movie_list:
            name = base_name + genre['name']
            code = f"discover.movie(with_genres={genre['id']})"
            self.make_list(name, code)

    def get_all(self):
        popular = self.make_list('Popular in Movies', 'tmdb.Movies().popular()')
        top_rated = self.make_list('Top Rated Movies', 'tmdb.Movies().now_playing()')
        self.upload_all_genres()

    def update_all(self, force_reset=False):
        if force_reset:
            self.remove_all()
        self.get_all()
        for item in self.resp:
            MovieList.objects.update_or_create(name=item['name'], defaults=item)

    @staticmethod
    def remove_all():
        MovieLists.remove_all()


if __name__ == '__main__':
    c = MovieLists()
    c.update_all(force_reset=False)

