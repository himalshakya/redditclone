"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote$', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote/$', views.downvote, name='downvote'),
    # url(r'^(?P<userid>[\d\w]+)/posts/$', views.user_posts, name='user_posts'),
    # url(r'^login/$', views.loginview, name='login'),
]
