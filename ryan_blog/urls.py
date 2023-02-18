from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #www.ryan-blog.com
    path('posts/', include('posts.urls')), #www.ryan-blog.com\posts\
    path('admin/', admin.site.urls),
]
