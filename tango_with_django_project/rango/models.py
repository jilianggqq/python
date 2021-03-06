#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import logging
logging.basicConfig(level=logging.DEBUG)
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    logging.debug('**********Category***************')
    c_id = models.AutoField(primary_key=True)
    # you use primary_key = True if you do not want to use default field "id" given by django to your model
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        logging.debug("******************Category saving...**************************")
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name + " " + str(self.views) + " " + str(self.likes)


class Page(models.Model):
    logging.debug('**********Page***************')
    p_id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

if __name__ == '__main__':
    logging.debug('__main__')
    c = Category()
    c.name = "test"
    print c
