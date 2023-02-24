# Imports the APIView Class from rest_framework
from rest_framework.views import APIView
# Response Class...
from rest_framework.response import Response

# Status input for serializers
# When returning Responses from HTTP requests!!
from rest_framework import status

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

# and the serializer from Serializers.py
from profiles_api import serializers
# Defines our logic for endpoints
from profiles_api import models
from profiles_api import permissions



class Hello(APIView):
	"""Test API View """
	# What data to except when we make HTTP requests
	# and in View is says name so expect an input of name _^
	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Return a list of APIView features"""
		an_apiview = [
			"Uses HTTP methods as function (get, post, patch, put and delete)",
			"IS similar to a traditional Django View",
			"Gives you the most control over your application logic",
			"Is mapped manually to URLs",
		]
		# so anything else will be an error trying to put in Response _^
		# Converts from string and objects (dictionaries) to Json file
		return Response({'message': "Hello!", "an_apiview": an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""
		serializer = self.serializer_class(data=request.data)


		if serializer.is_valid():
			# Retrive from Serializers
			name = serializer.validated_data.get('name')
			last_name = serializer.validated_data.get('last_name')
			message = f'Hello {name} {last_name}'
			return Response({'message': message})
		else:
			return Response(
				'Errors: ', serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	#pk meaning: is for ID...
	def put(self, request, pk=None):
		"""Handle updating an object"""
		# Put would replace everything
		# it would remove the first name complitely _^
		return Response({"method": 'PUT'})

	def patch(self, request, pk=None):
		"""Handle a partial update of an object"""
		# only updating the field provided in the request
# example if i were to have a field of fist name and last
# if i would make  a patch request to update just the last name it
# would only update the last name _^
		return Response({'method': "PATCH"})

	def delete(self, request, pk=None):
		"""Delete an object"""
		return Response({'method': 'DELETE'})

# on API View you do them to control the HTTP methods
# that u wanna support on your endpoint






"""VIEW SETS"""
class HelloViewSets(viewsets.ViewSet):
	"""Test Api ViewSet"""
	# Here you add actions that u would like to preform on a typical API

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a Hello message"""
		a_viewset = [
			'Uses actions (list, create, retrieve, update, patrial_update)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code'
		]

		return Response({'message': 'Hello ViewSet!','a_viewset': a_viewset})

	def create(self, request):
		"""Create a new hello message"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			last_name = serializer.validated_data.get('last_name')
			message = f"Hello {name} {last_name}"
			return Response({"message": message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)


		def retrieve(self, request, pk=None):
			"""Handle getting an object by its ID"""
			return Response({'http_method': "GET"})


		def update(self, request, pk=None):
			"""Handle updating an object"""
			return Response({"http_method": "PUT"})

		def partial_update(self, request, pk=None):
			"""Handle updating part of an object"""
			return Response({"http_method": "PATCH"})

		def destroy(self, request, pk=None):
			"""Handle removing an object"""
			return Response({"http_method": "DELETE"})



class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handle creating and updating profiles"""
# 	Here we need to provide a query set to the ModelViewSet so it will wich object in the database are gonna be managed
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	"""The Django Rest Framework knows the standard function that you would want
	to preform on a model viewset and that is the
	create function to create new items
	list function to list the models that are in the data base
	the update, partial update and destroy to manage specific model objects in the data base
	Django Does all of this for us just by
	 assigning serializer class to a model serializer and the query set
	 this is aswome about ModelViewSet"""

	"""How is authenticated"""
	authentication_classes = (TokenAuthentication,) #dont forget about the comma so this gets created as a tuple instead of a single item

	"""What kind of permissions does he has"""
	permission_classes = (permissions.UpdateOwnProfile,)




