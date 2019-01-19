from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('evento/<int:evento_id>/', views.detalle, name='detalle'),


    # path('usuario/<slug:usuario_id>/', views.usuario, name='usuario'),

    path('usuario/<int:usuario_id>/', views.usuario_detail, name='usuario_detail'),
    path('usuario/new/', views.usuario_new, name='usuario_new'),
    path('usuario/<int:usuario_id>/edit/', views.usuario_edit, name='usuario_edit'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)