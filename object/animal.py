#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Animal(object):

    def run(self):
        print 'Animal is running...'


class Dog(Animal):

    def run(self):
        super(Dog, self).run()
        print 'Dog is running...'

a = Animal()
a.run()

d = Dog()
d.run()
