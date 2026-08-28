from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome  = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    ativa = models.BooleanField(default=True)

    def __string__(self):
        return self.nome
