from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        # fields = ('nombre', 'apellido1',)
        fields = '__all__'
        # exclude = ('created_by',)