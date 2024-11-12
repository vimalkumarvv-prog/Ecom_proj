from django.test import TestCase


class TestURL(TestCase):

    def testhomeurl(self):
        response = self.client.get('/add_product/')
        print(response)
        self.assertEqual(response.status_code, 200)
