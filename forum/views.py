from django.shortcuts import render
from .models import Entry, Message

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