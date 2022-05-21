from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UsuarioForm

# Create your views here.


def inicio(request):
    return render(request, 'base.html', {})


def novo_usuario(request):
    template_name = 'usuarios/novo_usuario.html'
    context = {}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('usuarios:usuario_login')
    else:
        form = UsuarioForm()
    context['form'] = form
    return render(request, template_name, context)


def usuario_login(request):
    template_name = 'usuarios/usuario_login.html'
    context = {}
    return render(request, template_name, context)
