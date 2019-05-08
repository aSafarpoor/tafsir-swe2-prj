from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'^course_list',views.CourseListAPIview.as_view()),
    #url(r'^course/create$', views.CourseCreateAPIView.as_view(), name='course-create'),
    url(r'^create',views.create),
    url(r'^change',views.change),
    url(r'^delete',views.delete),
]

