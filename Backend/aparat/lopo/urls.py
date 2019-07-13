from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lopo import views

urlpatterns = [
    path('aparat/', views.call_aparat),
    # path('aparat/<int:pk>', views.aparat_detail),
]
