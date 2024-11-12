from django.test import TestCase, Client
from django.urls import reverse, resolve
# from home.models import Product
from home.views import home, signin


# class TestView(TestCase):
#     def testview(self):
#         client = Client()
#         response = client.get(reverse('home'))
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')

class TestView(TestCase):
    def setUp(self):  ##setup method: to run group test or individual test we have to use this method,To write pre defined codes
        self.client = Client()
        self.home = reverse('home')
        self.signin = reverse('signin')

    def testviewhome(self):
        response = self.client.get(self.home)
        print('Response: ', response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def testviewsignin(self):
        response = self.client.get(self.signin)
        print('Response: ', response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_in.html')
