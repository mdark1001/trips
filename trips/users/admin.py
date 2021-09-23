"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 23/09/21
@name: admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    """Custom user admin for app user and model User """
    list_display = ['first_name', 'middle_name', 'last_name', 'email', 'is_staff', 'is_client']
    list_filter = ('is_client', 'is_verified', 'create_date')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile Admin  """

    def show_user_emial(selfI, record):
        return record.user.email

    list_display = ('user', 'show_user_emial')
    search_fields = ('user__first_name', 'user__email', 'user__middle_name', 'user_last_name')
    show_user_emial.short_description = 'email'


admin.site.register(User, CustomUserAdmin)
