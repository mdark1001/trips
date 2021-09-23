"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 23/09/21
@name: Profile
"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from trips.utils.AppModel import AppModel
from .User import User


class Profile(AppModel):
    """ User profile   """

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    picture = models.ImageField(
        'Profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True,
    )
    biography = models.TextField(
        verbose_name='Biography',
        max_length=500,
        blank=True,
    )

    # Agregar otros datos del perfil...

    def __str__(self):
        """ Represent user """
        return str(self.user)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """

    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)

