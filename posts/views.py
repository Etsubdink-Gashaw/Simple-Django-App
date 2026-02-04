from django.shortcuts import render, redirect, get_object_or_404
from .models import Post



def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(
                title=title,
                content=content
            )

        return redirect('home')
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'posts/home.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})    