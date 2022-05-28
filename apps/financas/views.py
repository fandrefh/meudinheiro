from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Categoria
from .forms import CategoriaForm

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
