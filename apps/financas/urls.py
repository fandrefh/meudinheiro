from django.urls import path

app_name = 'financas'

from . import views

urlpatterns = [
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('editar-categoria/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('apagar-categoria/<int:pk>/', views.apagar_categoria, name='apagar_categoria'),
    path('nova-receita/', views.nova_receita, name='nova_receita'),
    path('lista-receitas/', views.lista_receitas, name='lista_receitas'),
    path('editar-receita/<int:pk>/', views.editar_receita, name='editar_receita'),
    path('apagar-receita/<int:pk>/', views.apagar_receita, name='apagar_receita'),
    path('nova-despesa/', views.nova_despesa, name='nova_despesa'),
    path('lista-despesas/', views.lista_despesas, name='lista_despesas'),
    path('editar-despesa/<int:pk>/', views.editar_despesa, name='editar_despesa'),
    path('apagar-despesa/<int:pk>/', views.apagar_despesa, name='apagar_despesa'),
    path('busca/', views.buscar, name='buscar'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('', views.principal, name='principal'),
]
