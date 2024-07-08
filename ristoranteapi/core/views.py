from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ristorante, Ricetta, Ingrediente
from .serializers import RistoranteSerializer, RicettaSerializer, IngredienteSerializer

class RistoranteViewSet(viewsets.ModelViewSet):
    """
    ViewSet per le operazioni CRUD su Ristorante e listing personalizzati.
    """
    queryset = Ristorante.objects.all()
    serializer_class = RistoranteSerializer

    @action(detail=False, methods=['get'])
    def per_ricetta(self, request):
        """
        Restituisce i ristoranti che cucinano una ricetta specifica.
        """
        ricetta_id = request.query_params.get('ricetta_id')
        if ricetta_id:
            ristoranti = Ristorante.objects.filter(ricette__id=ricetta_id)
            serializer = self.get_serializer(ristoranti, many=True)
            return Response(serializer.data)
        return Response({"error": "Specificare un ID ricetta"})

class RicettaViewSet(viewsets.ModelViewSet):
    """
    ViewSet per le operazioni CRUD su Ricetta e listing personalizzati.
    """
    queryset = Ricetta.objects.all()
    serializer_class = RicettaSerializer

    @action(detail=False, methods=['get'])
    def per_ristorante(self, request):
        """
        Restituisce le ricette di un ristorante specifico.
        """
        ristorante_id = request.query_params.get('ristorante_id')
        if ristorante_id:
            ricette = Ricetta.objects.filter(ristoranti__id=ristorante_id)
            serializer = self.get_serializer(ricette, many=True)
            return Response(serializer.data)
        return Response({"error": "Specificare un ID ristorante"})

    @action(detail=False, methods=['get'])
    def per_ingrediente(self, request):
        """
        Restituisce le ricette che contengono un ingrediente specifico.
        """
        ingrediente_id = request.query_params.get('ingrediente_id')
        if ingrediente_id:
            ricette = Ricetta.objects.filter(ingredienti__id=ingrediente_id)
            serializer = self.get_serializer(ricette, many=True)
            return Response(serializer.data)
        return Response({"error": "Specificare un ID ingrediente"})

class IngredienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet per le operazioni CRUD su Ingrediente e listing personalizzati.
    """
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    @action(detail=False, methods=['get'])
    def per_ricetta(self, request):
        """
        Restituisce gli ingredienti di una ricetta specifica.
        """
        ricetta_id = request.query_params.get('ricetta_id')
        if ricetta_id:
            ingredienti = Ingrediente.objects.filter(ricette__id=ricetta_id)
            serializer = self.get_serializer(ingredienti, many=True)
            return Response(serializer.data)
        return Response({"error": "Specificare un ID ricetta"})

    @action(detail=False, methods=['get'])
    def per_ristorante(self, request):
        """
        Restituisce gli ingredienti utilizzati da un ristorante specifico.
        """
        ristorante_id = request.query_params.get('ristorante_id')
        if ristorante_id:
            ingredienti = Ingrediente.objects.filter(ricette__ristoranti__id=ristorante_id).distinct()
            serializer = self.get_serializer(ingredienti, many=True)
            return Response(serializer.data)
        return Response({"error": "Specificare un ID ristorante"})