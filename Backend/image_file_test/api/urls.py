

from django.conf.urls import url , include
from . import views

urlpatterns = [
    # url(r'^course_list',views.CourseListAPIview.as_view()),
    #url(r'^section_list',views.SectionListAPIview.as_view()),
    #url(r'^course/create$', views.CourseCreateAPIView.as_view(), name='course-create'),
    url(r'^create1',views.create1.as_view()),
    url(r'^create0',views.create0),
    url(r'^call',views.call),
    url(r'^gmi',views.get_movie_id),
    url(r'^list',views.ListAPIview.as_view()),
    
]

