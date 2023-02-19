from django.db import models
from django.contrib.auth.models import AbstractBaseUser #Users
from django.contrib.auth.models import PermissionsMixin #Permission
from django.contrib.auth.models import BaseUserManager #Manager

# Manager

class UserProfileManager(BaseUserManager):
	"""Manager for user profiles"""
	def create_user_function(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError("User must have an email address")

# 		Normalize the email adress to all normal letters (small)
#       Standarize every email a small case
		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		# Hashing the password (encrypting it)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, email, name, password):
		"""Create and save a new superuser with given details"""
		user = self.create_user_function(email, name, password)
		# is_superuser is automatically create by PermissionsMixin in the UserProfile model bellow
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database model for user in the system"""

	# We don't wanna allow two users to use the same email adress
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)

	# If we ever need to deactivate a user we can do it like this
	is_active = models.BooleanField(default=True)

	# To determine if user is a stuff user that has access to Django Admin etc..
	is_staff = models.BooleanField(default=False)

	# Module Manager (must be objects)
	objects = UserProfileManager()

	# This is for instead of providing username and password we're taking the
	# email from email field and they'll provide the email instead of username
	# so username_field is now EmailField ;)

	USERNAME_FIELD  = 'email'
	# At minimum the user must specify the email address and the name!
	REQUIRED_FIELDS = ['name']


# 	Django to interact with our custum module
# 	Because we're defining a function in a class must call self ;)
	def get_full_name(self):
		"""Retrive Full Name Of User"""
		return self.name

	def get_short_name(self):
		"""Retrive short name of user"""
		return self.name

	# RECOMMANDED FOR ALL DJANGO MODULES
	def __str__(self):
		"""Return string representation of our user"""
		return self.email
"""Doing all theese Functions to use integration with other components in django _^"""