from .views import showFeed, showFollowingFeed, MakePostView, ViewPost, UpvotePost
from django.urls import path

urlpatterns = [
    path('feed', showFeed, name='showFeed'),
    path('following', showFollowingFeed, name='showFollowingFeed'),
    path('add', MakePostView, name='makePost'),
    path('view/<int:post_id>', ViewPost, name='viewPost'),
    path('upvote/<int:post_id>', UpvotePost, name='upvotePost'),
]