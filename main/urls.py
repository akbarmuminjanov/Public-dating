from django.urls import path
from .views import home, create_post, post_detail, send_message, inbox

urlpatterns = [
    path("", home, name='home'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('message/new/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
]

