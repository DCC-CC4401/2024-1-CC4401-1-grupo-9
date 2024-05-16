from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Login, Register, ForgetPassword
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'GET':
        #mostramos la pagina
        return render(request, 'login.html', {
        'form': Login
        })

    elif request.method == 'POST':
        form = Login(request.POST)
        #validamos los datos
        validacion = True
        if validacion:
            #redirigimos al foro (home por mientras)
            return redirect('/')
        else:
            #aviso y que intente de nuevo
            return render(request, 'login.html', {
            'form': Login
            })

def register_view(request):
    if request.method == 'GET':
        #mostramos la página
        return render(request, 'register.html', {
            'form': Register
        })

    
    elif request.method == 'POST':
        print(request.POST)
        form = Register(request.POST)
        print("valid  "+str(form.is_valid())+"\n")
        print("errors  "+str(form.errors)+"\n")
        print("bound   "+str(form.is_bound)+"\n")
        
        #validamos los datos
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Te registraste EXITOsamente')
            login(request,user)
            # acá se agrega un nuevo estudiante a la db
            # Estudiante.objects.create(username = request.POST['username'],
            #                           password = request.POST['password1'],
            #                           rol = "1",
            #                           email = request.POST['email'])
            # probablemente redirigimos al login
            return redirect('/login/')
        else:
            return render(request, 'register.html', {
            'form': Register
            })

def forgot_password_view(request):
    return render(request, 'forgot-password.html', {
        'form': ForgetPassword
    })

def home_view(request):
    return render(request, 'home.html')