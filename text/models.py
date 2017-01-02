from django.db import models

# Create your models here.
class AbouTxt(models.Model):
	txt = models.CharField(max_length=600)

	def __unicode__(self):
		return self.txt

class DecTxt(models.Model):
	title = models.CharField(max_length=10)
	txt = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class ClassTxt(models.Model):
	title = models.CharField(max_length=10)
	txt = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class Worker(models.Model):
	job = models.CharField(max_length=5)
	name = models.CharField(max_length=5)