from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'password.html')

def home(request):
    return render(request, 'home.html')