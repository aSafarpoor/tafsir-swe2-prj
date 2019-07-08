from django.conf.urls import url , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^list',views.ListAPIview.as_view()),
    url(r'^contact',views.contactAPIview.as_view()),
    url(r'^news',views.newsAPIview.as_view()),
    # url(r'^create',views.CreateAPIview.as_view()),
    # url(r'^edit/(?P<id>\w{0,50})/$',views.EditAPIview.as_view()),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)