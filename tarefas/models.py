from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    concuilda = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
