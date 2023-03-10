from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'blogger', 'comments_count', 'likes_count', 'post_date', 'is_published')
  list_display_links = ['id', 'title']
  list_editable = ['is_published']
  list_filter = ['blogger']
  search_fields = ['title', 'text', 'blogger__name']
  readonly_fields = ['comments_count', 'likes_count']
  list_per_page = 20

admin.site.register(Post, PostAdmin)
