from django.urls import path

app_name = 'usuarios'

from . import views

urlpatterns = [
    path('novo/', views.novo_usuario, name='novo_usuario'),
    path('login/', views.usuario_login, name='usuario_login'),
    path('', views.inicio, name='inicio'),
]
