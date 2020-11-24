from django.db import models
from typing import Iterable


class ListField(models.TextField):
    """
     A custom Django field to represent lists as comma separated strings
     """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert (isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(str(value))


class CreatedBy(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField()
    credit_id = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    gender = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    profile_path = models.CharField(max_length=100, default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField(default=None)
    name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.name


class LastEpisodeToAir(models.Model):
    item_id = models.AutoField(primary_key=True)

    air_date = models.DateField(default=None, null=True, blank=True)
    episode_number = models.PositiveSmallIntegerField()
    id = models.PositiveIntegerField(default=None, null=True, blank=True)
    name = models.CharField(max_length=150)
    overview = models.TextField(default=None, null=True, blank=True)
    production_code = models.CharField(max_length=100)
    season_number = models.PositiveIntegerField()
    # show_id = models.PositiveIntegerField()
    still_path = models.CharField(max_length=100, default=None, null=True, blank=True)
    vote_average = models.FloatField(default=None, null=True, blank=True)
    vote_count = models.PositiveIntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class NextEpisodeToAir(models.Model):
    item_id = models.AutoField(primary_key=True)

    air_date = models.DateField(default=None, null=True, blank=True)
    episode_number = models.PositiveSmallIntegerField()
    id = models.PositiveIntegerField(default=None, null=True, blank=True)
    name = models.CharField(max_length=150)
    overview = models.TextField(default=None, null=True, blank=True)
    production_code = models.CharField(max_length=100)
    season_number = models.PositiveIntegerField()
    # show_id = models.PositiveIntegerField()
    still_path = models.CharField(max_length=100, default=None, null=True, blank=True)
    vote_average = models.FloatField(default=None, null=True, blank=True)
    vote_count = models.PositiveIntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Networks(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    logo_path = models.CharField(max_length=50, null=True, default=None)
    origin_country = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'{self.name}'


class Seasons(models.Model):
    item_id = models.AutoField(primary_key=True)
    id = models.PositiveIntegerField()
    air_date = models.DateField(default=None, null=True, blank=True)
    episode_count = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    name = models.CharField(max_length=150)
    overview = models.TextField(default=None, null=True, blank=True)
    poster_path = models.CharField(max_length=50, default=None, blank=True, null=True)
    season_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class ProductionCompanies(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField()
    name = models.CharField(max_length=150, default=None)
    logo_path = models.CharField(max_length=50, null=True, default=None)
    origin_country = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'{self.name}'


class ProductionCountries(models.Model):
    air_date = models.DateField(default=None, null=True, blank=True)
    name = models.CharField(max_length=150, default=None)
    iso_3166_1 = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'{self.name}'


class SpokenLanguages(models.Model):
    english_name = models.CharField(max_length=255, default=None, null=True)
    name = models.CharField(max_length=150, default=None)
    iso_639_1 = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'{self.name}'


class Videos(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.CharField(max_length=200, default=None)
    iso_639_1 = models.CharField(max_length=10, default=None)
    iso_3166_1 = models.CharField(max_length=10, default=None)
    key = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=150, default=None)
    site = models.CharField(max_length=100, default=None)
    size = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.name}({self.site})"


class Show(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField()
    backdrop_path = models.CharField(max_length=100, default=None, null=True, blank=True)
    # Many to Many Fields
    created_by = models.ManyToManyField(CreatedBy, related_name='created_by')

    episode_run_time = ListField(default=None, null=True, max_length=500)
    first_air_date = models.DateField(default=None, null=True, blank=True)
    # Many to Many Field
    genres = models.ManyToManyField(Genres, related_name='genres_for_tv', default=None)

    homepage = models.URLField(max_length=350, null=True, blank=True)
    # tmdb_id = models.PositiveIntegerField(default=None, blank=False)
    in_production = models.BooleanField(null=True, default=None)
    languages = ListField(default=None, null=True, max_length=500)
    last_air_date = models.DateField(default=None, null=True, blank=True)

    last_episode_to_air = models.ForeignKey(LastEpisodeToAir, on_delete=models.DO_NOTHING, default=None, null=True)
    name = models.CharField(max_length=150)
    # Many to Many Field
    #  next_episode_to_air = models.CharField(max_length=20, default=None, null=True)
    next_episode_to_air = models.ForeignKey(NextEpisodeToAir, on_delete=models.DO_NOTHING, null=True)
    # Many to Many Field
    networks = models.ManyToManyField(Networks, related_name='networks')

    number_of_episodes = models.PositiveSmallIntegerField()
    number_of_seasons = models.PositiveSmallIntegerField()
    origin_country = ListField(default=None, null=True, max_length=500)
    original_language = models.CharField(max_length=20, default=None, blank=True)
    original_name = models.CharField(max_length=100, default=None)
    overview = models.TextField(default=None, null=True, blank=True)
    popularity = models.FloatField(default=None)
    poster_path = models.CharField(max_length=50, default=None, blank=True, null=True)
    # Many to Many Field
    production_companies = models.ManyToManyField(ProductionCompanies, related_name='production_companies_for_tv',
                                                  default=None)
    production_countries = models.ManyToManyField(ProductionCountries, related_name='production_countries_for_tv',
                                                  default=None)
    seasons = models.ManyToManyField(Seasons, related_name='seasons')

    status = models.CharField(max_length=50, null=True, default=None, blank=True)
    type = models.CharField(max_length=50, null=True, default=None, blank=True)
    vote_average = models.FloatField(default=None, null=True, blank=True)
    vote_count = models.PositiveIntegerField(default=None, null=True, blank=True)

    # Content Rating
    rating = models.CharField(max_length=5, null=True, default=None, blank=True)
    iso_3166_1 = models.CharField(max_length=5, null=True, default=None, blank=True)

    # Trailer
    videos = models.ManyToManyField(Videos, related_name='videos_tv', default=None)

    tagline = models.CharField(max_length=255, default=None, null=True, blank=True)
    spoken_languages = models.ManyToManyField(SpokenLanguages, related_name='spoken_languages_for_tv', default=None, blank=True)

    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        return self.name
