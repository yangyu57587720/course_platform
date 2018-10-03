from rest_framework import serializers
from app01 import models


class CourseOutlineSerializers(serializers.ModelSerializer):
    """课题大纲序列化"""

    class Meta:
        model = models.CourseOutline
        fields = ["id", "title", "content"]


class CourseDetailSerializers(serializers.ModelSerializer):
    """课程详情序列化"""
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ["id", "hours", "why_study", "teachers"]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{"id": row.id, "name": row.name, "title": row.title, "role": row.get_role_display()} for row in queryset]


class CourseSerializers(serializers.ModelSerializer):
    """专题课程序列化"""
    course_type = serializers.CharField(source="get_course_type_display")
    level = serializers.CharField(source="get_level_display")

    class Meta:
        model = models.Course
        fields = ["id", "name", "level", "course_img", "course_type"]


class DegreeCourseSerializers(serializers.ModelSerializer):
    """学位课程序列化"""
    class Meta:
        model = models.DegreeCourse
        fields = ["id", "name", "course_img", "brief", "period"]


class ArticleViewSetSerializers(serializers.ModelSerializer):
    """文章序列化"""
    source = serializers.CharField(source="source.name")
    article_type = serializers.CharField(source="get_article_type_display")
    position = serializers.CharField(source='get_position_display')

    class Meta:
        model = models.Article
        fields = ["title", "source", "article_type", 'head_img', 'brief', 'pub_date', 'comment_num', 'agree_num',
                  'view_num', 'collect_num', 'position']


class ArticleDetailViewSetSerializers(serializers.ModelSerializer):
    """文章详情序列化"""
    class Meta:
        model = models.Article
        fields = ['title', 'pub_date', 'agree_num', 'view_num', 'collect_num', 'comment_num', 'source', 'content',
                  'head_img']





