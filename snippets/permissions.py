from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    只允许用户编辑自己的字段
    """

    def has_object_permission(self, request, view, obj):
        # 允许所有的读请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅允许用户对自己的文件进行写操作
        return obj.owner == request.user