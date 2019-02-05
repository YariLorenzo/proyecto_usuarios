from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from. models import Evento, Usuario
from .forms import UsuarioForm

# ------------------ CHART.JS IMPORT
from random import shuffle, randint
from itertools import islice
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from chartjs.colors import next_color, COLORS
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartPieView, HighChartDonutView

# -----------------------------------

@login_required
def index(request):

    lista_ult_eventos = Evento.objects.order_by('-fecha')[:5]
    # contador_votos = Item.objects.filter(votes__contest=contestA).count()
    template = loader.get_template('votaciones/lista_eventos.html')
    context = {
        'lista_ult_eventos' : lista_ult_eventos,
    }
    return HttpResponse(template.render(context, request))
@login_required
def lista_usuarios(request):
    lista_usuarios = Usuario.objects.all()
    # contador_votos = Item.objects.filter(votes__contest=contestA).count()
    return render(request, 'votaciones/lista_usuarios.html', {'lista_usuarios': lista_usuarios})

@login_required
def usuarios_evento(request, evento_id):
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


@login_required
def lista_eventos(request):

    lista_ult_eventos = Evento.objects.order_by('-fecha')[:5]
    # contador_votos = Item.objects.filter(votes__contest=contestA).count()
    template = loader.get_template('votaciones/lista_eventos_est.html')
    context = {
        'lista_ult_eventos' : lista_ult_eventos,
    }
    return HttpResponse(template.render(context, request))

# ------------------ GRAFICOS ------------------------------------------------
class ColorsView(TemplateView):
    template_name = 'votaciones/colors.html'

    def get_context_data(self, **kwargs):
        data = super(ColorsView, self).get_context_data(**kwargs)
        data['colors'] = islice(next_color(), 0, 50)
        return data


class ChartMixin(object):
    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 random dataset to plot."""
        def data():
            """Return 7 randint between 0 and 100."""
            return [randint(0, 100) for x in range(7)]

        return [data() for x in range(3)]

    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)


class ColumnHighChartJSONView(ChartMixin, BaseColumnsHighChartsView):
    title = _('Column Highchart test')
    yUnit = '%'
    providers = ['All']
    credits = {"enabled": False}

    def get_data(self):
        return [super(ColumnHighChartJSONView, self).get_data()]


class LineChartJSONView(ChartMixin, BaseLineChartView):
    pass


class LineHighChartJSONView(ChartMixin, HighchartPlotLineChartView):
    title = _('Line HighChart Test')
    y_axis_title = _('Kangaroos')

    # special - line charts credits are personalized
    credits = {
        'enabled': True,
        'href': 'http://example.com',
        'text': 'Novapost Team',
    }


class PieHighChartJSONView(ChartMixin, HighChartPieView):
    pass


class DonutHighChartJSONView(ChartMixin, HighChartDonutView):
    pass


# Pre-configured views.
colors = ColorsView.as_view()

column_highchart_json = ColumnHighChartJSONView.as_view()
line_chart = TemplateView.as_view(template_name='votaciones/grafico.html')
line_chart_json = LineChartJSONView.as_view()
line_highchart_json = LineHighChartJSONView.as_view()
pie_highchart_json = PieHighChartJSONView.as_view()
donut_highchart_json = DonutHighChartJSONView.as_view()