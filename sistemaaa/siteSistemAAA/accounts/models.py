from django.db import models

# Create your models here.

class Client(models.Model):
    cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)

    def create_client(self):
        self.save()

    def __str__(self):
        return self.nome