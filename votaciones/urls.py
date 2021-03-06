from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('inicio/', views.index, name='index'),
    path('estadisticas/', views.lista_eventos, name='lista_eventos'),
    # path('login/', auth_views.LoginView.as_view(template_name='votaciones/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # ex: /polls/5/
    path('evento/<int:evento_id>/', views.usuarios_evento, name='lista_eventos'),


    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),

    path('usuario/<int:usuario_id>/', views.usuario_detail, name='usuario_detail'),
    path('usuario/new/', views.usuario_new, name='usuario_new'),
    path('usuario/<int:usuario_id>/edit/', views.usuario_edit, name='usuario_edit'),

    path('grafico/',views.line_chart, name = 'line_chart'),
    path('grafico/json/',views.line_chart_json, name = 'line_chart_json')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)