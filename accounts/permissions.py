from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'admin'

class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'member'


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admin users to perform all actions,
    but members can only perform read actions (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        # Allow any authenticated user to perform SAFE_METHODS
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        
        # Allow only admin users to perform other methods
        return request.user.is_authenticated and request.user.user_type == 'admin'

