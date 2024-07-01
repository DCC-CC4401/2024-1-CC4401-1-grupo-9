from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Entry, Message
from .forms import ForumEntry, ForumMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

""" 
Vista para manejar los foros
"""
@login_required
def forum(request: HttpRequest, entry_id: int = None) -> (HttpResponseRedirect | HttpResponsePermanentRedirect):


    if request.method == 'GET':
        # Si el metodo es GET, se renderiza el template correspondiente 
        if entry_id:
            # Si se pasa un id de entrada, se renderiza el template de foro 
            forum = Entry.objects.filter(id=entry_id).reverse()
            msgs = Message.objects.filter(entry_id=entry_id).order_by('created_at').reverse()
            return render(request=request, 
                          template_name='forum.html',
                          context={'forum': forum, 
                                   'messages': msgs, 
                                   'form': ForumMessage})
        else:
            # Si no se pasa un id de entrada, se renderiza el template de foros 
            forums = Entry.objects.all().order_by('created_at').reverse()
            return render(request=request,
                          template_name='forums_main.html',
                          context={'forums': forums, 
                                   'form': ForumEntry})

    elif request.method == 'POST':
        # Si el metodo es POST, se procesa el formulario correspondiente 

        if entry_id:
            # Si se pasa un id de entrada, se procesa el formulario de mensaje 
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
            # Si no se pasa un id de entrada, se procesa el formulario de entrada 
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
 
"""
Vista para manejar la API de foros. 
Esta vista permite obtener los foros en formato JSON
"""
def api_forums(request: HttpRequest) -> JsonResponse:

    if request.method == 'GET':
        entry_id = request.GET.get('entry_id', None)
        if entry_id:
            # Si se pasa un id de entrada, se obtienen los mensajes 
            forum = Entry.objects.filter(id=entry_id)
            if (forum):
                messages = Message.objects.filter(entry_id=entry_id).order_by('created_at').reverse()
                data = {
                    'forum': {
                    'id': forum[0].id,
                    'title': forum[0].title,
                    'body': forum[0].body,
                    'created_at': forum[0].created_at
                    },
                    'messages': [
                        {'id': msg.id, 'message': msg.message, 'created_at': msg.created_at} 
                        for msg in messages
                    ]
                }
            else:
                data = {}

        else:
            #Si el metodo es GET, se obtienen los foros
            forums = Entry.objects.all().order_by('created_at').reverse()
            title = request.GET.get('title', None)

            #Si se pasa un titulo, se filtran los foros por el titulo 
            if title:
                forums = forums.filter(title__icontains=title)

            data = [
                {'id': forum.id, 'title': forum.title, 'body': forum.body, 'created_at': forum.created_at} 
                for forum in forums
            ]
        
        return JsonResponse(data, safe=False)