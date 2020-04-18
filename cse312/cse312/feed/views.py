from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comments
from cse312.users.models import User
from .forms import PostForm, CommentForm
from django.http import Http404, HttpResponseRedirect

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
    comments = Comments.objects.filter(post = post)
    form = CommentForm(request.POST or None)
    args = {
    'post':post,
    'comments':comments,
    'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.post = post
            f.user = request.user
            f.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form = CommentForm()
    return render(request, 'feed/post.html', args)

@login_required
def UpvotePost(request, post_id):
    post = Post.objects.get(id = post_id)
    post.upvotes.add(request.user)
    return render(request, 'feed/post.html', {'post':post})

@login_required
def MakeComment(request, post_id):
    pass