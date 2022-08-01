from django.contrib import admin
from django.urls import path, include

from blog.views import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

handler404 = "blog.views.handler404"
