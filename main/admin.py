from django.contrib import admin
from .models import Post, Comment, Message
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author']

admin.site.register(Comment)
admin.site.register(Message)
