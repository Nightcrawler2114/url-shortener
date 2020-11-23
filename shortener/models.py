from django.db import models


class UrlObject(models.Model):

    long_url = models.URLField(max_length=300)
    short_url = models.CharField(max_length=200, blank=True)
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):

        return f'Long url: {self.long_url} Short url: {self.short_url}'
