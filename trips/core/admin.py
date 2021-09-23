"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 21/09/21
@name: admin.py
"""
from django.contrib import admin

from .models.trip_category import TripCategory


@admin.register(TripCategory)
class AdminTripCategory(admin.ModelAdmin):
    """ Admin model for TripCategory Model in core app"""
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
