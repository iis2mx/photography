from django.shortcuts import render
def baby(request):
    return render(request, 'gallery/baby.html')
def product(request):
    return render(request, 'gallery/product.html')
def country(request):
    return render(request, 'gallery/country.html')