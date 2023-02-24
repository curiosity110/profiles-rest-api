from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
	"""Allow user to edit their own profile"""

	def has_object_permission(self, request, view, obj):
		"""Check use is trying to edit their own profile"""
		print(permissions.SAVE_METHODS)
		# if the request.method (HTTP GET request) is in the permissions of safe methods return True
		if request.method in permissions.SAVE_METHODS:
			return True

		# if obj.id is same and the requested user are the same person return true
		return obj.id == request.user.id # is this whole line ture? if not return false