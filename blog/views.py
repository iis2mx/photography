from .models import blog
from django.shortcuts import render
def blog(request):
    post=blog.objects.all

    return render(request, 'blog/blog.html',{'post':post})