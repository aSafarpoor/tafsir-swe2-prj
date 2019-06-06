from django.urls import include, path
from django.contrib import admin
from VideoSend import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aparat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),


]
