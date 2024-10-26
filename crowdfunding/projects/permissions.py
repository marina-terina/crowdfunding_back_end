from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user
    
class IsSuperhero(permissions.BasePermission):
    """
    Custom permission to only allow users with superhero status to view the user list.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a superhero
        return request.user.is_authenticated and request.user.is_superuser