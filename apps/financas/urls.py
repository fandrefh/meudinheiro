from django.urls import path

app_name = 'financas'

from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
]
