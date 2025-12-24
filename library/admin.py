from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter=['name', 'surname', 'year','biografy']
    list_display=['name', 'surname', 'year', 'biografy']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter=['title', 'description', 'publish_year']
    list_display=['title', 'description', 'publish_year']


    def get_author(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    get_author.short_description = "авторы"
