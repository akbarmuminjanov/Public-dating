from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Message
from .forms import PostForm, CommentForm, MessageForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})

