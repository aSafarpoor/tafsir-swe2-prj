from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lopo import views

urlpatterns = [
    path('snippets/', views.call_aparat),
    # path('snippets/<int:pk>', views.snippet_detail),
]
