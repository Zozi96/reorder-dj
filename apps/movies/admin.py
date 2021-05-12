from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class Admin(admin.ModelAdmin):
    list_display = ('lookup_id', 'order',)
