from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
  if request.method == 'POST':
    # Register User
    print('yes it is POST method')
    messages.error(request, 'This is a test for error message.')
    return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Login User
    pass
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')


