from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	user_name = models.CharField(max_length=120)
	course_name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return self.course_name



class Coin(models.Model):
	user_name = models.CharField(max_length=120)
	coin = models.CharField(max_length=50)


	def __unicode__(self):
		return self.user_name



class Document(models.Model):
	course_id = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	img = models.ImageField(blank=True)


	def __unicode__(self):
		return self.title