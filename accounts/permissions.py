from rest_framework.permissions import BasePermission


class Facilitator(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_staff

class Instructor(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return bool(request.user.is_staff and request.user.is_superuser)

class Instructor_Facilitator(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.user.is_staff)

