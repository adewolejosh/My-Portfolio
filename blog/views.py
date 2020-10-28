from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


# Create your views here.
class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True, drafted=False)


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    query_slug = True
