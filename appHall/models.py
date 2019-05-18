from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
	"""
	This extends django.contrib.auth
	Model to represent generic user.
	"""
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	# def __str__(self):
	# 	return '%s, %s' % (self.last_name, self.first_name)

	# def __str__(self):
	# 	return '%s, %s' % (self.state, self.country)


class Hall(models.Model):
	"""
	Model to represent a hall.
	"""
	name = models.CharField(
	    max_length=200,
	    help_text='Enter the name of place',
	    null=False,
	    blank=False)
	location = models.CharField(
	    max_length=200,
	    help_text='Enter location direction')
	num_seat = models.IntegerField(
	    help_text='Enter number of seats',
	    db_column='Seat capacity',
	    null=False)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('User', on_delete=models.CASCADE)

	def __str__(self):
	    return self.name




class Owner(models.Model):
	user_count = models.ForeignKey('User', on_delete=models.CASCADE)
	is_owner = models.BooleanField()
	name_company = models.CharField(max_length=100, null=True, blank=True, help_text='Your company name, optional')

	def __str__(self):
		return '%s, %s' % (self.user_count.last_name, self.user_count.first_name)


class Event(models.Model):
	name_event = models.CharField(max_length=100, help_text='The title of your event')
	start_event = models.DateTimeField(auto_now=False, editable=True, help_text='Enter date and hour')
	end_event = models.DateTimeField(auto_now=False, editable=True, help_text='Enter date and hour')
	creator_event = models.ForeignKey(User)
	hall_event = models.ForeignKey(Hall)

	def __str__(self):
		return self.name_event


class Coment(models.Model):
	coment = models.TextField()
	date_coment = models.DateTimeField()
	user = models.ForeignKey(User)
	hall = models.ForeignKey(Hall)

	def __str__(self):
		return self.user