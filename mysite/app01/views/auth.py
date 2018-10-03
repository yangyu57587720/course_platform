from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01 import models


class TestAuth(BaseAuthentication):
    """验证用户登录组件"""
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserAuthToken.objects.filter(token=token).first()
        if not obj:
            return AuthenticationFailed({'code': 1001, 'error': '认证失败'})
        return obj.user.username, obj
