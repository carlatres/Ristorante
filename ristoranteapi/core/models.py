from django.db import models


class Ristorante(models.Model):
    """
    Modello per rappresentare un ristorante.
    """
    nome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Ricetta(models.Model):
    """
    Modello per rappresentare una ricetta.
    """
    nome = models.CharField(max_length=100)
    ristoranti = models.ManyToManyField(Ristorante, related_name='ricette')

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    """
    Modello per rappresentare un ingrediente.
    """
    nome = models.CharField(max_length=100)
    ricette = models.ManyToManyField(Ricetta, related_name='ingredienti')

    def __str__(self):
        return self.nome