from django.contrib import admin
from .models import Entry, Message, Message_votes, Entry_votes

# Register your models here.
admin.site.register(Entry)

admin.site.register(Message_votes)

# Clase para mostrar los votos de los mensajes en el panel de admin
class EntryVotesAdmin(admin.ModelAdmin):
    list_display = ('entry', 'user', 'vote_display')
    
    def vote_display(self, obj):
        return 'Upvote' if obj.vote == 1 else 'Downvote'
    vote_display.short_description = 'Vote'

admin.site.register(Entry_votes, EntryVotesAdmin)

# Clase para mostrar los mensajes en el panel de admin
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'entry_id')  # Mostrar message y entry_id en las columnas

    def entry_id(self, obj):
        return obj.entry_id  # Retorna el ID de la entrada asociada a este mensaje

    entry_id.short_description = 'Entry ID'  # Etiqueta para la columna del panel de admin

admin.site.register(Message, MessageAdmin)
