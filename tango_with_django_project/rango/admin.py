#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from rango.models import Category, Page
from rango.models import UserProfile

# admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'c_id', 'url')

# Add in this class to customized the Admin Interface


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
