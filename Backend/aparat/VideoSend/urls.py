from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'aparat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('postvideo/', admin.site.urls),


]
