from django import forms

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    # nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Categoria
        # fields = ['nome', 'descricao', 'tipo']
        # fields = '__all__'
        exclude = ['usuario']


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', required=True)
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())
