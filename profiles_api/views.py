# Imports the APIView Class from rest_framework
from rest_framework.views import APIView
# Response Class...
from rest_framework.response import Response

# Status input for serializers
# When returning Responses from HTTP requests!!
from rest_framework import status

# and the serializer from Serializers.py
from profiles_api import serializers
# Defines our logic for endpoints
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

