# permissions.py
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or obj.country.user == request.user or obj.state.country.user == request.user
