from TMDB.pure_tmdb import RealTMDb
from home.models import ShowList


class AllShowList(RealTMDb):
    resp = []

    def __init__(self):
        super().__init__()

    def add_to_resp(self, item):
        self.resp.append(item)

    def make_list(self, name, code):
        item = {'name': name, 'code': f'i.items = tmdb.{code}["results"]'}
        self.add_to_resp(item)
        return item

    def upload_all_genres(self):
        show_list = self.tmdb.Genres().tv_list()['genres']
        base_name = 'Shows Popular in '
        for genre in show_list:
            name = base_name + genre['name']
            code = f"Discover().tv(with_genres={genre['id']})"
            self.make_list(name, code)

    def get_all(self):
        popular = self.make_list('Popular in Shows', 'TV().popular()')
        today_airing = self.make_list('Shows Airing Today', 'TV().airing_today()')
        top_rated = self.make_list('Top Rated Shows', 'TV().top_rated()')
        self.upload_all_genres()

    def update_all(self):
        self.get_all()
        for item in self.resp:
            ShowList.objects.update_or_create(name=item['name'], defaults=item)


if __name__ == '__main__':
    c = AllShowList()
    c.update_all()
