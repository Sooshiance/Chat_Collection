from django.contrib import admin

from .models import Room, UserActivity


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'pk', 'last_activity')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

admin.site.register(Room, RoomAdmin)

admin.site.register(UserActivity, UserActivityAdmin)
