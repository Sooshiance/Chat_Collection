from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class Admin(UserAdmin):
    list_display = ('phone', 'username', 'is_active', 'pk',)
    filter_horizontal = ()
    list_filter = ('is_active',)
    fieldsets = ()
    search_fields = ('username', 'phone')
    list_display_links = ('phone', 'username')


admin.site.register(User, Admin)
