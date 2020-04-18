from .views import showFeed, MakePostView, ViewPost, UpvotePost
from django.urls import path

urlpatterns = [
    path('', showFeed, name='showFeed'),
    path('add', MakePostView, name='makePost'),
    path('view/<int:post_id>', ViewPost, name='viewPost'),
    path('upvote/<int:post_id>', UpvotePost, name='upvotePost'),
]