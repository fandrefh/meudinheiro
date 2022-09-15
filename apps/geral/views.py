from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from movimentacoes.models import Movimentacao
from .forms import CategoriaForm, LoginForm, UserForm
from .models import Categoria

# Create your views here.


@login_required
def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})


def login_usuario(request):
    template_name = 'geral/login_usuario.html'
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            usr = authenticate(username=usuario, password=senha)
            if usr:
                login(request, usr)
                return redirect('geral:principal')
            else:
                messages.error(request, 'Usuário ou senha inválido')
                return redirect('geral:login_usuario')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def logout_usuario(request):
    logout(request)
    return redirect('geral:login_usuario')


def novo_usuario(request):
    template_name = 'geral/novo_usuario.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password) # 123 -> %$#*9)&
            f.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('geral:login_usuario')
        else:
            messages.error(request, 'Corrija os erros do seu formulário')
            form = UserForm(request.POST)
            context['form'] = form
            return render(request, template_name, context)
    else:
        form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def nova_categoria(request):
    template_name = 'geral/nova_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso.')
            return redirect('geral:lista_categorias')
        else:
            form = CategoriaForm(request.POST)
            context['form'] = form
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_categorias(request):
    template_name = 'geral/lista_categorias.html'
    # categorias = Categoria.objects.all()  # SQL: SELECT * FROM geral_categoria; <-- tudo, idependente do dono
    # SQL: SELECT * FROM geral_categoria WHERE usuario = 'admin';
    categorias = Categoria.objects.filter(usuario=request.user)  # <--- somente do usuário admin
    context = {
        'categorias': categorias,
    }
    return render(request, template_name, context)


def relatorio(request):
    template_name = 'geral/relatorio.html'
    data_inicial = request.GET.get('data-inicial', timezone.now())
    data_final = request.GET.get('data-final', timezone.now())
    movimentacoes = Movimentacao.objects.filter(usuario=request.user, data_criacao__gte=data_inicial, data_criacao__lte=data_final)  # lookup
    context = {
        'movimentacoes': movimentacoes,
    }
    return render(request, template_name, context)
