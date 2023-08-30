from django.test import TestCase
from client.models import Client

class ClientTestCase(TestCase):
    def setUp(self) -> None:
        Client.objects.create(first_name="John",last_name="Oliver",company_name="some company")
        return super().setUp()
    
    def test_getting_a_Client(self):
        aClient=Client.objects.get(first_name='John')
        self.assertEqual(aClient.company_name,"some company")

