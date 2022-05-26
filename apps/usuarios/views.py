from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UsuarioForm, UsuarioLogin

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
    if request.method == 'POST':
        form = UsuarioLogin(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login feito com sucesso')
                    return redirect('financas:principal')
                else:
                    messages.warning(request, 'Sua conta foi inativada.')
                    return redirect('usuarios:usuario_login')
            else:
                messages.error(request, 'Usuário ou senha inválido.')
                return redirect('usuarios:usuario_login')
    else:
        form = UsuarioLogin()
        context['form'] = form
    return render(request, template_name, context)


def usuario_logout(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('usuarios:usuario_login')
