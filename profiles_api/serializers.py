from rest_framework import serializers

# importing model from profiles_api users
from profiles_api import models

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field for testing our APIView"""

	name = serializers.CharField(max_length=10)
	last_name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
	"""SErializer a user profile object"""
	# Models for a specific model in our meta class
	class Meta:
		model = models.UserProfile  # so it points to our userProfile models
# 		list of field in our models to manage in our serializer
# theese are fields to make them accessible in our API
# or to create new models with our Serializer
		fields = ('id', 'email', 'name', 'password') # Tuple of fields
# 		But we want to make an exception to password because we wnat to use it
#  only when creating new users in the system... we don't want the users to be able to retrieve the password hasshed
# 		the way to do that is using extra_kwargs of dictionary of the fields that u wanna configure
		extra_kwargs = {
			'password': {
				'write_only': True, # so you can only use that to create new objects and not retrieve
			# 	so when we do a GET you want to see your password field included in that request

			# 	For Browse API, to set the password with dots ^__^
				'style': {'input_type': 'password'}
			}
		}

# We need to overwrite the function create to create_user function so that way we can hash our pw
		def create(self, validated_data):
			"""Create and return a new user"""
			user = models.UserProfile.objects.create_user(
				email=validated_data['email'],
				name=validated_data['name'],
				password=validated_data['password'],
			)

			return user






