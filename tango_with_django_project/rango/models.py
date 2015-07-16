#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import logging
logging.basicConfig(level=logging.DEBUG)
# Create your models here.


class Category(models.Model):
    logging.debug('**********Category***************')
    c_id = models.AutoField(primary_key=True)
    # you use primary_key = True if you do not want to use default field "id" given by django to your model
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name


class Page(models.Model):
    logging.debug('**********Page***************')
    p_id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title

if __name__ == '__main__':
    logging.debug('__main__')
    c = Category()
    c.name = "test"
    print c
