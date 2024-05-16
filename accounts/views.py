from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Login, Register, ForgetPassword
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def login(request):
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

def register(request):
    if request.method == 'GET':
        #mostramos la página
        return render(request, 'register.html', {
            'form': Register
        })

    elif request.method == 'POST':
        form = Register(request.POST)
        #validamos los datos

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.succes(request, 'Te registraste EXITOsamente')
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

def forgot_password(request):
    return render(request, 'forgot-password.html', {
        'form': ForgetPassword
    })

def home(request):
    return render(request, 'home.html')