import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from app01.models import Account, UserAuthToken
from utils.data_response import DataResponse


class loginView(APIView):
    """
    用于用户认证相关接口
    """

    def post(self, request, *args, **kwargs):
        """
        用户认证
        :param request: 请求相关的数据
        :param args: URL传参
        :param kwargs: URL关键字传参
        :return:
        """
        ret = DataResponse()
        try:
            user = request.data.get('user')
            pwd = request.data.get('pwd')
            user = Account.objects.filter(username=user, password=pwd).first()
            if not user:
                ret.code = 1001
                ret.error = '用户名或密码错误'
                return Response(ret)

            uid = str(uuid.uuid4())
            # 更新或创建用户，添加默认字符串
            UserAuthToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret.data = uid
        except Exception as e:
            ret.code = 1003

        return Response(ret.dict)
