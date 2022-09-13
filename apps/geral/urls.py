from django.urls import path

app_name = 'geral'

from geral import views

urlpatterns = [
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('', views.principal, name='principal'),
]
