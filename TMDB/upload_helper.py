from movie.models import (
    Movie, ProductionCountries,
    BelongsToCollection, SpokenLanguages,
)
from tv.models import (
     Show, Seasons, CreatedBy, NextEpisodeToAir, LastEpisodeToAir,
    Networks)


class UploadTMDB:
    def __init__(self):
        super().__init__()

    # Upload Movie to our Local DB
    def upload_movie_to_local_db(self, movie) -> Movie:
        # Movie.objects.all().delete()
        # Importing Same name field ;)
        from movie.models import Genres, ProductionCompanies, Videos

        # Removing Empty Items -> List/Dict
        self.remove_empty_items(movie)

        # Get All Many to Many Field Item
        mtmfi = self.get_many_to_many_item(movie)
        # print(f'Mtmfi -> {mtmfi}')

        # Get All Foreign Key Item
        fki = self.get_foreign_key_item(movie)

        # for i in mtmfi + fki:
        #     x = eval(self.snake_to_camel(i))
        #     x.objects.all().delete()

        movie_copy = movie.copy()

        # Removing mtmfi items first
        for i in mtmfi:
            movie_copy.pop(i)

        # Getting Foreign key inst
        fki_inst = {}
        for i in fki:
            try:
                # For Debugging
                # print(f'In -> {i}')

                fki_inst[i] = \
                    eval(self.snake_to_camel(i)).objects.update_or_create(defaults={'id': movie[i]['id']}, **movie[i])[
                        0]
            except NameError:
                print("-<Make Sure You Have Imported Your Model Class and Their are exatly in Camel Case Refer "
                      "self.snake_to_camel method")

        # Assigning fki keys in movie -> their instance
        for i in movie_copy.keys():
            if i in fki:
                movie_copy[i] = fki_inst[i]


        movie_inst = Movie.objects.update_or_create(defaults=movie_copy, id=movie_copy['id'])[0]

        # Finally Adding mtmfi inst
        for li in mtmfi:
            for i in movie[li]:
                try:
                    item = eval(self.snake_to_camel(li)).objects.update_or_create(**i)[0]
                    to = getattr(movie_inst, li.lower())
                    to.add(item)
                except ValueError as e:
                    print("Make Sure You Have Imported Your Model Class and Their are exactly in Camel Case (Refer "
                          "self.snake_to_camel method)" + str(e))
        return movie_inst

    # Upload Movie to our Local DB
    def upload_tv_to_local_db(self, tv):
        # Show.objects.all().delete()
        # Importing Same name field ;)
        from tv.models import Genres, ProductionCompanies, Videos, ProductionCountries, SpokenLanguages

        # Removing all the empty items
        self.remove_empty_items(tv)

        # Get All Many to Many Field Item
        mtmfi = self.get_many_to_many_item(tv)

        # Get All Foreign Key Item
        fki = self.get_foreign_key_item(tv)
        # for i in mtmfi + fki:
        #     x = eval(self.snake_to_camel(i))
        #     x.objects.all().delete()

        tv_copy = tv.copy()

        # Removing mtmfi items first
        for i in mtmfi:
            tv_copy.pop(i)

        # Getting Foreign key inst
        fki_inst = {}
        # print(f'FKi -> {fki}, TV -> {tv_copy}')
        for i in fki:
            try:
                fki_inst[i] = eval(self.snake_to_camel(i)).objects.update_or_create(**tv[i])[0]
            except NameError:
                print("-<Make Sure You Have Imported Your Model Class and Their are exatly in Camel Case Refer "
                      "self.snake_to_camel method")

        # Assigning fki keys in movie -> their instance

        for i in tv_copy.keys():
            if i in fki:
                tv_copy[i] = fki_inst[i]

        # List
        self.clean_list(tv_copy)

        tv_inst, was_created = Show.objects.update_or_create(defaults=tv_copy, id=tv_copy['id'])

        # Finally Adding mtmfi inst
        for li in mtmfi:
            for i in tv[li]:
                try:
                    item = eval(self.snake_to_camel(li)).objects.update_or_create(**i)[0]
                    to = getattr(tv_inst, li.lower())
                    to.add(item)
                except SyntaxError:
                    print("Make Sure You Have Imported Your Model Class and Their are exatly in Camel Case Refer "
                          "self.snake_to_camel method for " + li.lower() + str(i))

        # if was_created:
        #     print(f'Uploading -> {tv["name"]}')

        return tv_inst

    # Check if the movie exists
    @staticmethod
    def check_movie_from_our_db(movie):
        movie = Movie.objects.filter(tmdb_id=movie['id'])
        if movie:
            return movie[0]
        return False

    # Check if the show exist
    @staticmethod
    def check_show_from_our_db(show):
        show = Show.objects.filter(tmdb_id=show['id'])
        if show:
            return show[0]
        return False

    # Check Movie List
    def check_movies_list_from_our_db(self, movies):
        resp = []
        for is_movie in movies:
            movie = self.check_movie_from_our_db(is_movie)
            if movie:
                resp.append(movie)
        return resp

    # Check Show List
    def check_shows_list_from_our_db(self, shows):
        resp = []
        for is_show in shows:
            show = self.check_show_from_our_db(is_show)
            if show:
                resp.append(show)
        return resp

    # From Dict only
    @staticmethod
    def remove_empty_items(item):
        for i in list(item.keys()):
            if isinstance(item[i], list) or isinstance(item[i], dict):
                if len(item[i]) == 0:
                    del item[i]
                    # For Debugging
                    # print(f'Empty item {i} is removed')

    @staticmethod
    def clean_list(item):
        for i in item.keys():
            if isinstance(item[i], list):
                if not isinstance(item[i][0], dict):
                    item[i] = [str(i) for i in item[i]]

    @staticmethod
    def get_many_to_many_item(item):
        k = []
        for i in item:
            if isinstance(item[i], list):
                if len(item[i]) > 0:
                    # print(f'{i} -> {len(item[i])}')
                    if isinstance(item[i][0], dict):
                        k.append(i)
        return k

    @staticmethod
    def get_foreign_key_item(item):
        return [i for i in item if isinstance(item[i], dict)]

    @staticmethod
    def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))



