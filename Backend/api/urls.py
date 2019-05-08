from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('course/', include('course_app.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('django.contrib.auth.urls')),
]
