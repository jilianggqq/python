#!/usr/bin/env python
# -*- coding: utf-8 -*-

class student(object):
	"""docstring for student"""
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def get_name(self):
		return self.__name
		
	def get_age(self):
		return self.__age

	def  is_old(self):
		if(self.__age>35):
			return 'old'
		elif (self.__age<10):
			return 'young'
		else:
			return 'medium'

	def __len__(self):
		return len(self.__name)

	def hasmethod(self, method):
		if(hasattr(self, method)):
			fn = getattr(self, method)
			fn()
		else:
			return 'no such method'


## test
stu=student('Zhangsan', 20)

print isinstance(stu, student)
print isinstance(stu, object)

print stu.get_age()
print stu.get_name()

# __len__的特殊性
print len(stu)
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir(stu)

print stu.is_old()

print stu.hasmethod('is_old')