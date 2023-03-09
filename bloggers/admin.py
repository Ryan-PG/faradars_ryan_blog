from django.contrib import admin

from .models import Blogger

class BloggerAdmin(admin.ModelAdmin):
  list_display = ('id', 'email', 'name', 'phone', 'birth_date', 'register_date', 'posts_cout')
  list_display_links = ['id', 'name', 'email']
  search_fields = ['name', 'email', 'phone']
  list_per_page = 10

admin.site.register(Blogger, BloggerAdmin)
