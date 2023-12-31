from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuItemViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.menu_item = MenuItem.objects.create(title='Test Item', price=10, inventory=5)

    def test_get_menu_items(self):
        url = '/api/menuitem/'  # Promijenite putanju prema vašoj konfiguraciji URL-ova
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Provjera da li je samo jedna stavka dobivena

        expected_data = MenuItemSerializer(self.menu_item).data
        self.assertEqual(response.data[0], expected_data)
