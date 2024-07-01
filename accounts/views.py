from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Login, Register, ForgetPassword
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

"""
Vista que permite recibir una petición de login para que un usuario ingrese y se autentifique
Puede recibir:
    Get: para renderizar la plantilla login.html
    Post: para enviar credenciales de autenticación
"""
def login_view(request):
    #Caso GET
    if request.method == 'GET':
        #mostramos la pagina
        return render(request, 'login.html', {
        'form': Login
        })

    #Caso POST
    elif request.method == 'POST':
        form = Login(request.POST)
        #validamos los datos
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Autenticamos
            user = authenticate(request, username=username, password=password)
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

"""
Vista que permite recibir una petición de resgistro para que una persona cree un usuario
Puede recibir:
    Get: para renderizar la plantilla register.html
    Post: para enviar datos de creación de usuario
"""
def register_view(request):
    #Caso GET
    if request.method == 'GET':
        #mostramos la página
        return render(request, 'register.html', {
            'form': Register
        })

    #Caso POST
    elif request.method == 'POST':
        print(request.POST)
        form = Register(request.POST)
        
        #validamos los datos
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            #Registramos al usuario
            user.save()
            messages.success(request, 'Te registraste EXITOsamente')
            login(request,user)
            return redirect('/login/')
        else:
            return render(request, 'register.html', {
            'form': Register
            })

"""
Vista para acceder al perfil de un usuario
Existen dos casos:
    1) No se entrega un id de usuario en la url: En este caso se devuelve el perfil del usuario que 
    realiza la petición.
    2) Se entrega un id de usuario en la url: En este caso se devuelve el perfil del usuario respectivo
    de acuerdo a el id de la url.
"""
@login_required
def profile(request,user_id=None):
    if request.method == 'GET':
        #Accedemos al perfil del usuario del id de la url
        if user_id:
            estudiante = Estudiante.objects.get(id = user_id)
        #Accedemos al perfil del estudiante que realiza la request
        else:
            estudiante = request.user

        context = {
            'estudiante': estudiante,
        }
        return render(request, 'profile.html',context)

"""
Vista que renderiza plantilla forgot-password.html

(Implementación futura)
"""
def forgot_password_view(request):
    return render(request, 'forgot-password.html', {
        'form': ForgetPassword
    })

"""
Vista que permite acceder a la plantilla home.html

(Implementación futura)
"""
def home_view(request):
    return render(request, 'home.html')