from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Estudiante


class EstudianteAdmin(UserAdmin):
    model = Estudiante
    list_display = ('username', 'email', 'first_name', 'last_name', 'total_answers', 'useful_answers', 'total_questions', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'total_answers', 'useful_answers', 'total_questions')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(Estudiante, EstudianteAdmin)