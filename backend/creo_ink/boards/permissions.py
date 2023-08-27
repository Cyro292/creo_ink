from rest_framework import permissions


class IsBoardOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.owner:
            return True
        return False
