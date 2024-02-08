# rango/admin.py

from django.contrib import admin
from .models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register the PageAdmin class with Django's admin interface
admin.site.register(Page, PageAdmin)

# Register the Category model
admin.site.register(Category)


