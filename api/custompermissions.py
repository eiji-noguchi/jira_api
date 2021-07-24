from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    '''タスクを消せるのはオーナーのみにするカスタムパーミッション'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # 値を変更しないリクエスト（GETメソッド）の場合許可
            return True
        return obj.owner.id == request.user.id
