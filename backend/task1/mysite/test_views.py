from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Restaurant

class RestaurantAPITests(APITestCase):
    
    def test_create_restaurant(self):
        url = reverse('restaurant-list-create')
        data = {
            "name": "Pasta Palace",
            "address": "123 Noodle Street",
            "phone_number": "555-1234",
            "rating": 4.5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Pasta Palace')
    
    def test_list_restaurants(self):
        url = reverse('restaurant-list-create')
        Restaurant.objects.create(name="Burger Barn", address="456 Burger Blvd", phone_number="555-5678", rating=4.0)
        Restaurant.objects.create(name="Pizza Place", address="789 Pizza Ave", phone_number="555-9101", rating=4.2)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Burger Barn')
        self.assertEqual(response.data[1]['name'], 'Pizza Place')
