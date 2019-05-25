from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
	"""
	Creating a custom User Model extending AbstractUser
	Represent generic user.
	"""
	is_tenant = models.BooleanField(default=False)
	is_owner = models.BooleanField(default=False)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	def __str__(self):
		return '%s, %s' % (self.user.last_name, self.user.first_name)


class Owner(models.Model):
	"""
	This model represent owner of hall.
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name_company = models.CharField(max_length=100, null=True, blank=True, help_text='Your company name, optional')

	def __str__(self):
		return '%s, %s' % (self.user.last_name, self.user.first_name)