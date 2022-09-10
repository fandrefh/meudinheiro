from django.urls import path

from . import views

app_name = 'movimentacoes'

urlpatterns = [
    path('minhas-movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('nova-movimentacao/', views.nova_movimentacao, name='nova_movimentacao'),
    path('editar-movimentacao/<int:pk>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('apagar-movimentacao/<int:pk>/', views.apagar_movimentacao, name='apagar_movimentacao'),
]
