from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission