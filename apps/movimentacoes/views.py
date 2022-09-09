from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import MovimentacaoForm
from .models import Movimentacao

# Create your views here.


def lista_movimentacoes(request):
    template_name = 'movimentacoes/lista_movimentacoes.html'
    movimentacoes = Movimentacao.objects.filter(usuario=request.user)
    context = {
        'movimentacoes': movimentacoes,
    }
    return render(request, template_name, context)


def nova_movimentacao(request):
    template_name = 'movimentacoes/nova_movimentacao.html'
    context = {}
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.success(request, 'Movimentação salva com sucesso')
            return redirect('movimentacoes:lista_movimentacoes')
        else:
            form = MovimentacaoForm(request.POST)
            context['form'] = form
    else:
        form = MovimentacaoForm()
    context['form'] = form
    return render(request, template_name, context)
