from django.contrib import admin

from .models import Usuario, Evento

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellido1','apellido2')
    search_fields = ('dni','nombre','apellido1','apellido2')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha','categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    filter_horizontal = ('votantes',)


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Evento,EventoAdmin)
