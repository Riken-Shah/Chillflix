from django.db import models


class BelongsToCollection(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField(default=None)
    name = models.CharField(max_length=150, null=True, default=None)
    poster_path = models.URLField(max_length=50, default=None, blank=True, null=True)
    backdrop_path = models.URLField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField(default=None)
    name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.name


class ProductionCompanies(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveIntegerField()
    name = models.CharField(max_length=150, default=None)
    logo_path = models.CharField(max_length=50, null=True, default=None)
    origin_country = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.name


class ProductionCountries(models.Model):
    name = models.CharField(max_length=100, default=None)
    iso_3166_1 = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.name


class SpokenLanguages(models.Model):
    iso_639_1 = models.CharField(max_length=10, default=None)
    name = models.CharField(max_length=100, default=None)
    english_name = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Videos(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.CharField(max_length=200, default=None, null=True, blank=True)
    iso_639_1 = models.CharField(max_length=10, default=None)
    iso_3166_1 = models.CharField(max_length=10, default=None)
    key = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=150, default=None)
    site = models.CharField(max_length=100, default=None)
    size = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.name}({self.site})"


class Movie(models.Model):
    item_id = models.AutoField(primary_key=True)

    adult = models.BooleanField(default=False)
    backdrop_path = models.SlugField(max_length=100, default=None, null=True, blank=True)
    belongs_to_collection = models.ForeignKey(BelongsToCollection, on_delete=models.DO_NOTHING, null=True, default=None,
                                              blank=True)
    budget = models.PositiveIntegerField(default=None)

    # Many to Many Field
    genres = models.ManyToManyField(Genres, related_name='genres', default=None)

    homepage = models.CharField(max_length=350, null=True, blank=True)
    id = models.PositiveIntegerField(default=None, blank=False)
    imdb_id = models.CharField(max_length=20, blank=True, null=True, default=None)
    original_language = models.CharField(max_length=20, default=None, blank=True)
    original_title = models.CharField(max_length=100, default=None)
    overview = models.TextField(default=None, null=True, blank=True)
    popularity = models.FloatField(default=None)
    poster_path = models.SlugField(max_length=100, default=None, blank=True, null=True)

    # Many to Many Field
    production_companies = models.ManyToManyField(ProductionCompanies, related_name='production_companies',
                                                  default=None)

    # Many to Many Field
    production_countries = models.ManyToManyField(ProductionCountries, related_name='production_countries',
                                                  default=None)

    release_date = models.DateField(default=None)
    revenue = models.BigIntegerField(default=None)
    runtime = models.PositiveIntegerField(default=None, null=True, blank=True)

    # Many to Many Field
    spoken_languages = models.ManyToManyField(SpokenLanguages, related_name='spoken_languages', default=None)

    status_choice = (
        ('Rumored', 'Rumored'),
        ('Planned', 'Planned'),
        ('In Production', 'In Production'),
        ('Post Production', 'Post Production'),
        ('Released', 'Released'),
        ('Canceled', 'Canceled')
    )
    status = models.CharField(choices=status_choice, max_length=15, default=None)
    tagline = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=100, default=None, null=True)
    video = models.BooleanField(default=False, null=True, blank=True)
    vote_average = models.FloatField(default=None, null=True, blank=True)
    vote_count = models.PositiveIntegerField(default=None, null=True, blank=True)

    # Adding Certification (US Only)
    certification = models.CharField(default=None, null=True, max_length=10, blank=True)
    certification_country = models.CharField(default=None, null=True, max_length=20, blank=True)

    videos = models.ManyToManyField(Videos, related_name='videos', default=None)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
