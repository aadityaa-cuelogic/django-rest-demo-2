from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""
	def has_obejct_permission(self, request, view, obj):
		# Custom permission to only allow owners of an object to edit it.
		# so we'll always allow GET, HEAD or OPTIONS requests
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner of the snippet.
		return obj.owner == request.user