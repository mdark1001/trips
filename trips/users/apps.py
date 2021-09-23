"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 22/09/21
@name: apps
"""
from django.apps import AppConfig


class UserAppConfig(AppConfig):
    """ User app config """
    name = 'trips.users'
    verbose_name = 'Users'
