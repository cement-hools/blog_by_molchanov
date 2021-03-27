from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, \
    ObjectDelete


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


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class PostDelete(ObjectDelete, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(ObjectDelete, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'blog/tags_list.html', context)
