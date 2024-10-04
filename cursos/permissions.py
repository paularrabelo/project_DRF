from rest_framework import permissions

class SuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuse:
                return True
            return False
        return True