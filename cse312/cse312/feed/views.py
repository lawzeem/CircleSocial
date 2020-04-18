from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comments
from cse312.users.models import User
from .forms import PostForm
from django.http import Http404

def showFeed(request):
    posts = Post.objects.all()
    args = {'posts' : posts}
    return render(request, 'feed/feed.html', args);

@login_required
def MakePostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('showFeed')
    else:
        form = PostForm()
        args = {'form' : form}
        return render(request, 'feed/add.html', args)

@login_required
def ViewPost(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'feed/post.html', {'post':post})

@login_required
def UpvotePost(request, post_id):
    post = Post.objects.get(id = post_id)
    post.upvotes.add(request.user)
    return render(request, 'feed/post.html', {'post':post})

@login_required
def MakeComment(request, post_id):
    pass