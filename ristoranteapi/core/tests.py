from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ristorante, Ricetta, Ingrediente


class RistoranteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ristorante_data = {'nome': 'Test Ristorante', 'indirizzo': 'Via Test, 1'}
        self.response = self.client.post(
            '/api/ristoranti/',
            self.ristorante_data,
            format="json")

    def test_api_can_create_a_ristorante(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_ristorante(self):
        ristorante = Ristorante.objects.get()
        response = self.client.get(
            f'/api/ristoranti/{ristorante.id}/',
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, ristorante)

    def test_api_can_update_ristorante(self):
        ristorante = Ristorante.objects.get()
        change_ristorante = {'nome': 'Nuovo nome', 'indirizzo': 'Nuovo indirizzo'}
        res = self.client.put(
            f'/api/ristoranti/{ristorante.id}/',
            change_ristorante,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_ristorante(self):
        ristorante = Ristorante.objects.get()
        response = self.client.delete(
            f'/api/ristoranti/{ristorante.id}/',
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class RicettaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ristorante = Ristorante.objects.create(nome='Test Ristorante', indirizzo='Via Test, 1')
        self.ricetta_data = {'nome': 'Test Ricetta', 'ristoranti': [self.ristorante.id]}
        self.response = self.client.post(
            '/api/ricette/',
            self.ricetta_data,
            format="json")

    def test_api_can_create_a_ricetta(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_ricette_per_ristorante(self):
        response = self.client.get(
            f'/api/ricette/per_ristorante/?ristorante_id={self.ristorante.id}',
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)


class IngredienteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ristorante = Ristorante.objects.create(nome='Test Ristorante', indirizzo='Via Test, 1')
        self.ricetta = Ricetta.objects.create(nome='Test Ricetta')
        self.ricetta.ristoranti.add(self.ristorante)
        self.ingrediente_data = {'nome': 'Test Ingrediente', 'ricette': [self.ricetta.id]}
        self.response = self.client.post(
            '/api/ingredienti/',
            self.ingrediente_data,
            format="json")

    def test_api_can_create_an_ingrediente(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_ingredienti_per_ricetta(self):
        response = self.client.get(
            f'/api/ingredienti/per_ricetta/?ricetta_id={self.ricetta.id}',
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_api_can_get_ingredienti_per_ristorante(self):
        response = self.client.get(
            f'/api/ingredienti/per_ristorante/?ristorante_id={self.ristorante.id}',
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
