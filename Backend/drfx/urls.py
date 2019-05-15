from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url 
from users.views import TeacherListView

urlpatterns = [
    #url(r'^teacher_list', TeacherListView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]


'''
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''
