from app01.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from app01.serializer import course
from app01.views.auth import TestAuth


class NewsPapers(ViewSetMixin, APIView):
    authentication_classes = [TestAuth, ]

    def list(self, request, *args, **kwargs):
        """文章主页显示"""
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Article.objects.all()
            ser = course.ArticleViewSetSerializers(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = Article.objects.filter(pk=pk).first()
            ser = course.ArticleDetailViewSetSerializers(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)


class AgreeView(ViewSetMixin, APIView):

    def post(self, request, *args, **kwargs):
        """点赞"""
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            from django.db.models import F
            obj = Article.objects.filter(id=pk).update(agree_num=F("agree_num") + 1)
            ret['data'] = obj.agree_num
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '点赞失败'
        return Response(ret)