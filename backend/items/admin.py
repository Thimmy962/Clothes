from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MajorCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fileds = ('name', 'category')
    ordering = ('-id',)


@admin.register(MinorCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category', 'name')
    search_fileds = ('name', 'category')
    ordering = ('-id',)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fileds = ('name', 'category')
    ordering = ('id',)