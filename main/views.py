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

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post.id)
    else:
        comment_form = CommentForm()
        return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'comment_form':comment_form})
    
@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form':form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages})