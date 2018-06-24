from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://'+ request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, "posts/create.html", { "message_error": "Title and URL are required fields"})

    else:
        return render(request, "posts/create.html")


def home(request):
    posts = Post.objects.order_by('-votes')
    return render(request, "posts/home.html", { 'posts': posts})

#    url(r'^(?P<pk>[0-9]+)/upvote$', views.upvote, name='upvote'),
#    url(r'^(?P<pk>[0-9]+)/downvote/$', views.downvote, name='downvote'),##
#

def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes += 1
        post.save()
        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes -= 1
        post.save()
        return redirect('home')

# .all #filter(author.username = username) #.order_by('-votes')
def user_posts(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user) 
    except User.DoesNotExist:
        return render(request, 'posts/home.html', { "message_error": "User does not exist"})
    return render(request, "posts/user_posts.html", { 'posts': posts, 'user_post': username })
