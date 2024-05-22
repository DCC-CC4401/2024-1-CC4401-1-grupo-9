from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Login, Register, ForgetPassword
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"El nombre de usuario es {username} ")
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)  # Iniciar la sesión del usuario
                print(f"Usuario {username} autenticado exitosamente")
                return redirect('/forum/') 
            else:
                return redirect('/login/')
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

@login_required
def profile(request,user_id=None):
    
    if request.method == 'GET':
        if user_id:
            estudiante = Estudiante.objects.get(id = user_id)
        else:
            estudiante = request.user

        context = {
            'estudiante': estudiante,
        }
        return render(request, 'profile.html',context)

def forgot_password_view(request):
    return render(request, 'forgot-password.html', {
        'form': ForgetPassword
    })

def home_view(request):
    return render(request, 'home.html')