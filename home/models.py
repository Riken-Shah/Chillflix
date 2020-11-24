from django.db import models


class MovieList(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)
    code = models.CharField(max_length=100, default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Movie List"
        verbose_name_plural = "Movies List"

    def __str__(self):
        return self.name


class ShowList(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)
    code = models.CharField(max_length=100, default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Show List"
        verbose_name_plural = "Shows List"

    def __str__(self):
        return self.name


class Genres(models.Model):
    item_id = models.AutoField(primary_key=True)

    id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=150, default=None, null=True)
    backdrop_path = models.SlugField(max_length=100, default=None, blank=True, null=True)
    type = models.CharField(max_length=50, default=None, blank=True, null=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return f'{self.name}({self.type})'
