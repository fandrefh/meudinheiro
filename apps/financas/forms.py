from django import forms

from .models import Categoria, Receita, Despesa


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ['usuario']


class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        exclude = ['usuario']

    def __init__(self, user=None, *args, **kwargs):
        super(ReceitaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='RC', usuario=user)


class DespesaForm(forms.ModelForm):

    class Meta:
        model = Despesa
        exclude = ['usuario']

    def __init__(self, user=None, *args, **kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='DP', usuario=user)
