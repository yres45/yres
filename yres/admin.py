# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:20:54 2019

@author: Yres
"""

from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)