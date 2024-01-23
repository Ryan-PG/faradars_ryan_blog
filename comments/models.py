from django.db import models
from datetime import datetime

from posts.models import Post

class Comment(models.Model):
  user_email = models.CharField(max_length=200)
  user_name = models.CharField(max_length=200)
  comment_date = models.DateTimeField(default=datetime.now, blank=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment_text = models.TextField()

  def __str__(self) -> str:
      return self.comment_text