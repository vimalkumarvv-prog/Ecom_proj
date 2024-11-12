from django.test import TestCase
from django.urls import reverse, resolve
from home.views import edit_product


class TestUrlReverse(TestCase):
    def testhomeurl(self):
        url = reverse('edit_product', args=edit_product)
        print('Resolve: ', resolve(url))
        self.assertEqual(resolve(url).func, edit_product)
