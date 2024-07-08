from rest_framework import serializers
from .models import Ristorante, Ricetta, Ingrediente

class RistoranteSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Ristorante.
    """
    class Meta:
        model = Ristorante
        fields = '__all__'

class RicettaSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Ricetta.
    """
    class Meta:
        model = Ricetta
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Ingrediente.
    """
    class Meta:
        model = Ingrediente
        fields = '__all__'