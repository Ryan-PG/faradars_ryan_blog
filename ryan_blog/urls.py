from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #www.ryan-blog.com
    path('admin/', admin.site.urls),
]
