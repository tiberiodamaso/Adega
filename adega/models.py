from django.db import models

class Adega(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=10)
    qtd_vinhos = models.IntegerField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Adega'
        verbose_name_plural = 'Adegas'