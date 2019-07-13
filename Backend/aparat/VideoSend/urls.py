from django.urls import include, path
from django.contrib import admin
from VideoSend import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include



urlpatterns = [
    path('upload/', views.simple_upload),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
