"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 22/09/21
@name: User
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from trips.utils.AppModel import AppModel

phone_number_validator = RegexValidator(
    regex=r'\+?1?\d{9,15}$',
    message='This phone look wrong'
)


class User(AppModel, AbstractUser):
    """ Custom user model for Trip api"""
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        error_messages={
            'unique': "A user with that email already exists",
        }
    )

    phone_number = models.CharField(
        verbose_name='Phone number',
        max_length=17,
        blank=True,
        validators=[phone_number_validator]
    )
    middle_name = models.CharField(
        verbose_name='Middle name',
        max_length=150,
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'middle_name', 'last_name']

    is_client = models.BooleanField(
        default=True,
        verbose_name='Is Client',
        help_text=""" Check if user is a client """
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name='Account verified'
    )

    def __str__(self):
        """ Str Method """
        return self.username

    def short_name(self):
        """ get shortname as username"""
        return self.username
