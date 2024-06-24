from django import forms
from .models import Post, Message, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'video']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']