from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin, ObjectCreateMixin


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create_form.html'


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'blog/tags_list.html', context)
