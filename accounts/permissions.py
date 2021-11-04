from rest_framework.permissions import BasePermission


class Facilitator(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_superuser

class Instructor(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_staff
