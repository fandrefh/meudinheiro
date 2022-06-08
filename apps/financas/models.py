from django.db import models
from django.contrib.auth.models import User

from .managers import CategoriaManager, ReceitaManager, DespesaManager

# Create your models here.


class Categoria(models.Model):
    TIPO_CAT_CHOICES = (
        ('RC', 'Receita'),
        ('DP', 'Despesa'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(verbose_name='Nome', max_length=70)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    tipo = models.CharField(verbose_name='Tipo', max_length=2, choices=TIPO_CAT_CHOICES)

    objects = CategoriaManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Receita(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.SET_NULL, null=True)
    cadastrada_em = models.DateTimeField(verbose_name='Cadastrada em', auto_now_add=True)
    atualizada_em = models.DateTimeField(verbose_name='Atualizada em', auto_now=True)

    objects = ReceitaManager()

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-cadastrada_em']

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    identificacao = models.CharField(verbose_name='Identificação', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.SET_NULL, null=True)
    cadastrada_em = models.DateTimeField(verbose_name='Cadastrada em', auto_now_add=True)
    atualizada_em = models.DateTimeField(verbose_name='Atualizada em', auto_now=True)

    objects = DespesaManager()

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        ordering = ['-cadastrada_em']

    def __str__(self):
        return self.identificacao
