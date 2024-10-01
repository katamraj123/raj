from django.test import TestCase



# Create your tests here.


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item



from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User





class ItemAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='rajdarlling', password='katamr1j')
        self.client.login(username='rajdarlling', password='katamr1j')  # Log in the user
        # Generate a token for this user
        self.token = Token.objects.create(user=self.user)

        # Set the token in the request headers for authentication
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a test item
        self.item = Item.objects.create(
            name="Test Item",
            description="This is a test item.",
            quantity=5
        )
        self.valid_payload = {
            'name': 'New Item',
            'description': 'This is a new item.',
            'quantity': 10
        }
        self.invalid_payload = {
            'name': '',
            'description': 'This is an invalid item.',
            'quantity': -1
        }

    def test_create_item(self):
        response = self.client.post(reverse('item-create'), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)  # 1 from setup + 1 created
        self.assertEqual(Item.objects.get(id=response.data['id']).name, 'New Item')

    def test_retrieve_item(self):
        response = self.client.get(reverse('item-detail', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        response = self.client.put(reverse('item-update', args=[self.item.id]), {
            'name': 'Updated Item',
            'description': 'This is an updated item.',
            'quantity': 15
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_delete_item(self):
        response = self.client.delete(reverse('item-delete', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)  # Ensure item is deleted

    
