from django.shortcuts import render, redirect


def not_found(request, exception):
    print(exception)
    return render(request, 'coming_soon.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')

def home(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product-detail.html')

