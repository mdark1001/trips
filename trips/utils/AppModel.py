"""
@author: Miguel Cabrera <mdark100>
@date: 09/21/2021
@name: AppModel.py
@description: Trips Model App principal model abstract
"""
from django.db import models


class AppModel(models.Model):
    """ TripsApi abstract model,
     contains fields for another models in this project.
     Like:
        create_uid(User)
        create_date(Datetimne)
        write_uid(User)
        write_date(Datetime)
     """

    create_date = models.DateTimeField(
        verbose_name='Created on',
        auto_now_add=True,
        help_text='Date  time on record was created',
    )

    write_date = models.DateTimeField(
        verbose_name='Created on',
        auto_now=True,
        help_text='Date  time on record was last modified',
    )

    class Meta:
        abstract = True
        # get_lastet_by ='create_date'
        ordering = ('-create_date', '-write_date')
