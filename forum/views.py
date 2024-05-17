from django.shortcuts import render
from .models import Entry, Message
from .forms import ForumEntry
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def forum(request, forum_id=None):

    ## TODO: agregar mensajes
    if request.method == 'GET':
        if forum_id:
            forum = Entry.objects.filter(id=forum_id)
            return render(request=request, 
                          template_name='forum.html',
                          context={'forum': forum})
        else:
            forums = Entry.objects.all()
            return render(request=request,
                            template_name='forums_main.html',
                            context={'forums': forums})
        
    elif request.method == 'POST':
        form = ForumEntry(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.save()
            messages.success(request, 'Entrada subida exitosamente')
            return redirect('/foro/')
        else:
            ##Modificar esto para manejar el caso en el que no es valido
            return render(request, 'forum.html', {
            'form': ForumEntry
            })
