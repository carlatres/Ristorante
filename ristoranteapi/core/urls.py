from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RistoranteViewSet, RicettaViewSet, IngredienteViewSet

router = DefaultRouter()
router.register(r'ristoranti', RistoranteViewSet)
router.register(r'ricette', RicettaViewSet)
router.register(r'ingredienti', IngredienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]