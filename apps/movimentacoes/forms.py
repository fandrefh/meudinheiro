from django import forms

from geral.models import Categoria
from .models import Movimentacao


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        exclude = ['usuario']

    def __init__(self, usuario, *args, **kwargs):
        super(MovimentacaoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        # SELECT * FROM categoria WHERE usuario = usuario
