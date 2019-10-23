from django.shortcuts import render
from .models import Post
from marketing.models import Newsletter

def index(request):
    featured = Post.objects.filter(featured = True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_newsletter = Newsletter()
        new_newsletter.email = email
        new_newsletter.save()
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html',  context)

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})
