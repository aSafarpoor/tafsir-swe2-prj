from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('users/', include('users.urls')),
    path('course/', include('course_app.api.urls')),
    path('aboutus/', include('aboutus_app.api.urls')),
    path('imfi/', include('image_file_test.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('login/', views.CustomLoginView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('rest-auth/registration/v2/', views.TeacherListView.as_view()),
    path('', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
