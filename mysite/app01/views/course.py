from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from app01.serializer import course
from app01 import models


class CourseOutlineList(ViewSetMixin, APIView):
    """课题大纲"""

    def list(self, request, *args, **kwargs):
        ret = {"code": 1000, "data": None}
        try:
            queryset = models.CourseOutline.objects.all()
            co = course.CourseOutlineSerializers(queryset, many=True)
            ret["data"] = co.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = "获取课程大纲失败"
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {"code": 1000, "data": None}
        try:
            pk = kwargs.get("pk")
            obj = models.CourseDetail.objects.filter(id=pk).first()
            obj_cd = course.CourseDetailSerializers(obj, many=False)
            ret["data"] = obj_cd.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = "获取大纲详情失败"
        return Response(ret)


class CourseList(ViewSetMixin, APIView):
    """专题课程"""

    def list(self, request, *args, **kwargs):
        ret = {"code": 1000, "data": None}
        try:
            queryset = models.Course.objects.all()
            cl = course.CourseSerializers(queryset, many=True)
            ret["data"] = cl.data
        except Exception as e:
            ret["code"] = 1001
            ret["data"] = "获取专题课程失败"
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {"code": 1000, "data": None}
        try:
            pk = kwargs.get("pk")
            obj = models.DegreeCourse.objects.filter(id=pk).first()
            obj_d = course.DegreeCourseSerializers(obj, many=False)
            ret["data"] = obj_d.data
        except Exception as e:
            ret["code"] = 1001
            ret["data"] = "获取专题课程详情失败"
        return Response(ret)


class DegreeCourseList(ViewSetMixin, APIView):
    """学位课程"""

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

