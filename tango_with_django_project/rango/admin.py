#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'c_id', 'url')


admin.site.register(Page, PageAdmin)
