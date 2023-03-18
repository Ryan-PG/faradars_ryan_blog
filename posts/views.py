from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

def index(request):
  posts_list = Post.objects.order_by('-post_date').filter(is_published = True)

  paginator = Paginator(posts_list, 3)
  page = request.GET.get('page')
  paged_posts_list = paginator.get_page(page)

  context = {
    'posts': paged_posts_list
  }
  
  return render(request, 'posts/posts.html', context)

def post(request, post_id:int):
  return render(request, 'posts/post.html')

def search(request):
  return render(request, 'posts/search.html')