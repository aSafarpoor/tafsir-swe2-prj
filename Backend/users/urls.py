from django.urls import include, path
from django.conf.urls import url , include
import os
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [   
    url(r'^teacher_list', views.TeacherListView.as_view()),
    url(r'^student_list', views.StudentListView.as_view()),
    url(r'^teacher_courses/(?P<choosed_id>\w{0,50})/$',views.JoinTable.as_view(),name='teacher_courses') ,
    url(r'^teacher_info/(?P<id>\w{0,50})/$', views.TeacherDetailsAPIView.as_view()),
    url(r'^register',views.register),
    url(r'^parts',views.multiple_section),
    url(r'^test',views.test),
    url(r'^course_info',views.get_own_course_info),
    
]



if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


