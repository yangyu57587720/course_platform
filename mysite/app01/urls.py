from django.conf.urls import url
from app01.views import course
from app01.views import user

urlpatterns = [
    url(r'^login/$', user.loginView.as_view()),

    url(r'course_outline/$', course.CourseOutlineList.as_view({"get": "list"})),
    url(r'outline_detail/(?P<pk>\d+)/$', course.CourseOutlineList.as_view({"get": "retrieve"})),

    url(r'course/$', course.CourseList.as_view({"get": "list"})),
    url(r'course/(?P<pk>\d+)/$', course.CourseList.as_view({"get": "retrieve"})),

    url(r'degree_course/$', course.DegreeCourseList.as_view({"get": "list"})),
]
