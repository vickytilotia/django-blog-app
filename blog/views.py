'''
docstring
'''
from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

    all_posts = Post.newmanager.all() #we used here the newmanager, which is custom created

    return render(request, 'index.html', {'posts': all_posts})
