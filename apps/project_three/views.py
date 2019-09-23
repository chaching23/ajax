from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import post
from django import forms


def index(request):
  
#   Fetch all posts and render full index page with form
  
  context = {
      'posts': post.objects.all(),
    #   'new_post_form' : PostForm()
  }
  return render(request, 'project_three/index.html', context)


def Post(request):
    if request.method == 'POST':

    # Create new post and redirect to posts_index route

        # bound_form = PostForm(request.POST)

    # Check valid description

        # if bound_form.is_valid():
        post.objects.create(description=request.POST['description'])

#         return redirect('posts')

# def get(request):


        context = {
                'posts': post.objects.all()
        }
        return render(request, 'project_three/posts_index.html', context)
