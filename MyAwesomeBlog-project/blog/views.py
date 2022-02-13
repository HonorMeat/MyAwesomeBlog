from django.shortcuts import render, get_object_or_404
from .models import Posts

def showblog(request):
    posts = Posts.objects
    return render(request, 'blog/blog.html', {'posts': posts})
def specific_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post':post})
