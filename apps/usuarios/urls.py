from django.urls import path

app_name = 'usuarios'

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
