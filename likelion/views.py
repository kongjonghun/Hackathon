from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request, 'likelion/first.html')

def second(request):
    return render(request, 'likelion/second.html')

def accounts(request):
    return render(request, 'likelion/accounts.html')

def blog(request):
    return render(request, 'likelion/blog.html')    

def login(request):
    return render(request, 'likelion/login.html')    