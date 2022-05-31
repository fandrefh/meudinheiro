from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Categoria, Receita
from .forms import CategoriaForm, ReceitaForm


# Create your views here.


@login_required(login_url='/usuarios/login')
def principal(request):
    template_name = 'financas/principal.html'
    context = {}
    return render(request, template_name, context)


def nova_categoria(request):
    template_name = 'financas/nova_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat_form = form.save(commit=False)
            cat_form.usuario = request.user
            cat_form.save()
            messages.success(request, 'Categoria adicionada com sucesso.')
            return redirect('financas:lista_categorias')
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)


def lista_categorias(request):
    template_name = 'financas/lista_categorias.html'
    categorias = Categoria.objects.filter(usuario=request.user) # ORM -> SELECT * FROM categorias WHERE usuario = username
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)


def editar_categoria(request, pk):
    template_name = 'financas/nova_categoria.html'
    context = {}
    # categoria = get_object_or_404(Categoria, id=pk) # ORM -> SELECT * FROM categoria WHERE id = pk
    # categoria = Categoria.objects.filter(pk=pk, usuario=request.user).first() # ORM -> SELECT * FROM categoria WHERE id = pk
    try:
        categoria = Categoria.objects.get(pk=pk, usuario=request.user) # ORM -> SELECT * FROM categoria WHERE id = pk
    except Categoria.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para editar a categoria informada.')
        return redirect('financas:lista_categorias')
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('financas:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    context['form'] = form
    return render(request, template_name, context)


def apagar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk, usuario=request.user) # ORM -> SELECT * FROM categoria WHERE id = pk
        categoria.delete()
    except Categoria.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para apagar a categoria informada.')
        return redirect('financas:lista_categorias')
    messages.info(request, 'Categoria apagada.')
    return redirect('financas:lista_categorias')


def nova_receita(request):
    template_name = 'financas/nova_receita.html'
    context = {}
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita_form = form.save(commit=False)
            receita_form.usuario = request.user
            receita_form.save()
            messages.success(request, 'Receita adicionada com sucesso')
            return redirect('financas:lista_receitas')
    else:
        form = ReceitaForm()
    context['form'] = form
    return render(request, template_name, context)


def lista_receitas(request):
    template_name = 'financas/lista_receitas.html'
    receitas = Receita.objects.filter(usuario=request.user)
    context = {
        'receitas': receitas
    }
    return render(request, template_name, context)
