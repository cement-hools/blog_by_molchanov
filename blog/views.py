from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from blog.models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


# def post_detail(request, slug):
#     # post = get_object_or_404(Post, slug=slug)
#     post = Post.objects.get(slug__iexact=slug)
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog/post_detail.html', context)


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        context = {
            'post': post,
        }
        return render(request, 'blog/post_detail.html', context)


class TagDetail(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        context = {
            'tag': tag,
        }
        return render(request, 'blog/tag_detail.html', context)

def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'blog/tags_list.html', context)


# def tag_detail(request, slug):
#     # tag = get_object_or_404(Tag, slug=slug)
#     tag = Tag.objects.get(slug__iexact=slug)
#     print(tag)
#     context = {
#         'tag': tag,
#     }
#     return render(request, 'blog/tag_detail.html', context)
