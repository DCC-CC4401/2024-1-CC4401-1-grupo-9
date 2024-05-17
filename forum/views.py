from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest
from django.shortcuts import render
from .models import Entry, Message
from .forms import ForumEntry, ForumMessage
from django.contrib import messages
from django.shortcuts import render, redirect



def forum(request: HttpRequest, entry_id: int = None) -> (HttpResponseRedirect | HttpResponsePermanentRedirect):
    """ Vista para manejar los foros """

    if not request.user.is_authenticated:
        """ Si el usuario no esta autenticado, se redirige al login """
        return redirect('/login')


    if request.method == 'GET':
        """ Si el metodo es GET, se renderiza el template correspondiente """
        if entry_id:
            """ Si se pasa un id de entrada, se renderiza el template de foro """
            forum = Entry.objects.filter(id=entry_id).reverse()
            msgs = Message.objects.filter(entry_id=entry_id).order_by('created_at').reverse()
            return render(request=request, 
                          template_name='forum.html',
                          context={'forum': forum, 
                                   'messages': msgs, 
                                   'form': ForumMessage})
        else:
            """ Si no se pasa un id de entrada, se renderiza el template de foros """
            forums = Entry.objects.all().order_by('created_at').reverse()
            return render(request=request,
                          template_name='forums_main.html',
                          context={'forums': forums, 
                                   'form': ForumEntry})

    elif request.method == 'POST':
        """ Si el metodo es POST, se procesa el formulario correspondiente """

        if entry_id:
            """ Si se pasa un id de entrada, se procesa el formulario de mensaje """
            form = ForumMessage(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.entry = Entry.objects.filter(id=entry_id)
                message.user = request.user
                message.save()
                messages.success(request, 'Mensaje subido exitosamente')
                return redirect('/forum/'+entry_id)
            else:
                ## TODO: Modificar esto para manejar el caso en el que no es valido
                return redirect('/forum/'+entry_id)

        else:
            """ Si no se pasa un id de entrada, se procesa el formulario de entrada """
            form = ForumEntry(request.POST)
            if form.is_valid():
                entrada = form.save(commit=False)
                entrada.user = request.user
                entrada.save()
                messages.success(request, 'Entrada subida exitosamente')
                return redirect('/forum/'+str(entrada.id))
            else:
                ## TODO: Modificar esto para manejar el caso en el que no es valido
                return redirect('/forum/')
