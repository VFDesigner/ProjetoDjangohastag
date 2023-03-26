from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin
#Esse ponto antes de models, significa que estou importando pasta na mesma pasta do admin
#Só necessario criar para visualizar um campo do User dentro do admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {'fields':('filme_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)


