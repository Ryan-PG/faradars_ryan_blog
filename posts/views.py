from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from comments.forms import CommentForm

from comments.models import Comment

from .models import Post

def index(request):
  posts_list = Post.objects.order_by('-post_date').filter(is_published = True)

  paginator = Paginator(posts_list, 6)
  page = request.GET.get('page')
  paged_posts_list = paginator.get_page(page)

  context = {
    'posts': paged_posts_list
  }
  
  return render(request, 'posts/posts.html', context)

def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  comments = Comment.objects.filter(post=post)
  form = CommentForm()

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      post.comments_count += 1
      post.save()
      return redirect('post', post_id=post_id)
        
  context = {
    'post': post, 'comments': comments, 'form': form
  }

  return render(request, 'posts/post.html', context)


def search(request):
  posts = Post.objects.order_by('-post_date').filter(is_published = True)

  if 'search_text' in request.GET:
    search_text = request.GET['search_text']

    if search_text:
      posts = posts.filter(Q(title__icontains=search_text)
                           | Q(text__icontains=search_text)
                           | Q(blogger__name__icontains=search_text))

  context = {
    'posts': posts
  }
  
  return render(request, 'posts/search.html', context)

def like_post(request, post_id):
  if not request.user.is_authenticated:
    return render(request, 'accounts/authentication_alert.html')
  
  post = get_object_or_404(Post, pk=post_id)
  blogger = request.user.blogger  # Assuming the user is authenticated

  if blogger in post.likers.all():
    post.likers.remove(blogger)
    post.likes_count -= 1
  else:
    post.likers.add(blogger)
    post.likes_count += 1

  post.save()
  
  return redirect('post', post_id=post_id)