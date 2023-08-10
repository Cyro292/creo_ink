from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object
        return obj.user == request.user


class CanAccessPaidAccountFeatures(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("core.paid_account")
