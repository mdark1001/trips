"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 21/09/21
@name: trip_category
"""
from django.db import models
from trips.utils.AppModel import AppModel


class TripCategory(AppModel):
    """Different categories of trips in the app this is a model can use in search and metrics """
    name = models.CharField(
        verbose_name='Categoría',
        max_length=120,
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        verbose_name='Etiqueta',
    )

    class Meta:
        verbose_name = 'Categoría de viajes'
        verbose_name_plural = 'Categorías de viajes'
