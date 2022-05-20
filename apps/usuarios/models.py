from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(verbose_name='Foto', upload_to='fotos')
    cpf = models.CharField(verbose_name='CPF', max_length=14, blank=True, null=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.user.first_name
