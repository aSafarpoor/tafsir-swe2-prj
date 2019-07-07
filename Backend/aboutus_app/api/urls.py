from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'^list',views.ListAPIview.as_view()),
    # url(r'^create',views.CreateAPIview.as_view()),
    # url(r'^edit/(?P<id>\w{0,50})/$',views.EditAPIview.as_view()),

]
