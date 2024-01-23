from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['user_name', 'user_email', 'comment_text']
    labels = {
      'user_email': 'ایمیل',
      'user_name': 'نام',
      'comment_text': 'کامنت',
      }
