from rest_framework.test import APITestCase

class ItemTests(APITestCase):
    def test_create_item(self):
        url = '/items/'
        data = {'name': 'Item1', 'description': 'Test item'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
