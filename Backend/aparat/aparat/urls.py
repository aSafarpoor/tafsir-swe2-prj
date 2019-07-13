from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'aparat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('api/v1/sendToAparat', include('lopo.urls')),
    path('api/v1/sendToDB', include('lopo.urls')),

]
