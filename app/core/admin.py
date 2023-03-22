"""
Django Admin customisation
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define Admin pages for users."""
    odrering = ['id']
    list_display = ['email', 'name']

admin.site.register(models.user, UserAdmin)