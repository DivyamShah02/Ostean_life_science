from django.shortcuts import render, redirect


def not_found(request, exception):
    print(exception)
    return render(request, 'coming_soon.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')
