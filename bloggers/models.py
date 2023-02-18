from django.db import models
from datetime import datetime

class Blogger(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')
  birth_date = models.DateField(default=datetime.now, blank=True)
  register_date = models.DateField(default=datetime.now, blank=True)
  posts_cout = models.IntegerField(default=0)
  description = models.TextField()
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.name
   
