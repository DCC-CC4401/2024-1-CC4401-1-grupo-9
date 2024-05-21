from django.contrib import admin
from .models import Entry, Message

# Register your models here.
admin.site.register(Entry)
admin.site.register(Message)