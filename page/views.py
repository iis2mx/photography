from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'page/home.html')
def about(request):
    return render(request, 'page/about.html')

def contact(request):
    return render(request, 'page/contact.html')
def blog(request):
    return render(request, 'blog/blog.html')
