from django.shortcuts import render

def index(request):
  return render(request, 'posts/posts.html')

def post(request):
  return render(request, 'posts/post.html')

def search(request):
  return render(request, 'posts/search.html')