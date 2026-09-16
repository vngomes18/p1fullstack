from django.db import models


class Livro(models.Model):
    class TipoAcervo(models.TextChoices):
        DIGITAL = 'DIGITAL', 'Digital'
        FISICO = 'FISICO', 'Físico'

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo_acervo = models.CharField(
        max_length=10,
        choices=TipoAcervo.choices,
        default=TipoAcervo.FISICO,
    )

    def __str__(self):
        return self.titulo
