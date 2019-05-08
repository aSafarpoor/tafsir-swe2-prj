from django.urls import include, path
from django.conf.urls import url , include

from . import views

urlpatterns = [   
    url(r'^user_list', views.UserListView.as_view()),
    url(r'^teacher_courses/(?P<choosed_id>\w{0,50})/$',views.JoinTable.as_view(),name='teacher_courses') ,
    url(r'^teacher_info/(?P<id>\w{0,50})/$', views.TeacherDetailsAPIView.as_view()),
]
