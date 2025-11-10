from django.contrib import admin
from .models import Movie, Review, Person, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'released')
    search_fields = ['title', 'description']
    list_filter = ('status', 'released',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Review)
admin.site.register(Person)
admin.site.register(Genre)
