from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from. models import Evento, Usuario
from .forms import UsuarioForm

def index(request):
    lista_ult_eventos = Evento.objects.order_by('-fecha')[:5]
    # contador_votos = Item.objects.filter(votes__contest=contestA).count()
    template = loader.get_template('votaciones/lista_eventos.html')
    context = {
        'lista_ult_eventos' : lista_ult_eventos,
    }
    return HttpResponse(template.render(context, request))

def lista_usuarios(request):
    lista_usuarios = Usuario.objects.all()
    # contador_votos = Item.objects.filter(votes__contest=contestA).count()
    return render(request, 'votaciones/lista_usuarios.html', {'lista_usuarios': lista_usuarios})


def usuarios_envento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    votantes = evento.votantes.all()
    return render(request, 'votaciones/lista_usuarios_evento.html', {'evento': evento,'votantes':votantes})

def usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    # form = UsuarioForm(request.POST or None, instance=usuario)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect('/thanks/')
    return render(request, 'votaciones/usuario.html', {'usuario': usuario})

def usuario_detail(request, usuario_id):
    
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    lista_votaciones_usuario = Evento.objects.filter(votantes= usuario_id)
    lista_eventos = Evento.objects.order_by('-fecha')
    # eventos_comunes = set(lista_votaciones_usuario) & set(lista_eventos)
    # print (eventos_comunes)
    print(usuario)
    print(lista_eventos)
    return render(request, 'votaciones/usuario_detail.html', {'usuario': usuario, 
                                                            'lista_eventos': lista_eventos,
                                                            'lista_votaciones_usuario': lista_votaciones_usuario})


def usuario_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('votaciones.views.usuario_detail', pk=usuario.id)
    else:
        form = UsuarioForm()
    return render(request, 'votaciones/usuario_edit.html', {'form': form})

# @login_required
def usuario_edit(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            messages.success(request, 'Form submission successful')
            return redirect('usuario_detail', usuario_id=usuario.id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'votaciones/usuario_edit.html', {'form': form, 'usuario':usuario})