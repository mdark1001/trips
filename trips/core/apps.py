"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 21/09/21
@name: apps
"""
from django.apps import AppConfig

from django.utils.translation import gettext as _


class CoreAppConfig(AppConfig):
    """ Core app config"""

    name = 'trips.core'
    verbose_name = 'Configuraciones'
