from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('phone', 'username', 'is_superuser')
    filter_horizontal = ()
    list_filter = ('is_superuser',)
    fieldsets = ()
    search_fields = ('phone', 'username')


admin.site.register(User, UserAdmin)
