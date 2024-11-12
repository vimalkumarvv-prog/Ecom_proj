from django.test import TestCase
from home.models import Product, Category


class TestModel(TestCase):
    def testModelProduct(self):
        category, created = Category.objects.get_or_create(name="mobile phone")
        product = Product.objects.create(name='iq mobile', slug='mobiles', desc='good', price=30000, category=category,
                                         stock=10)
        self.assertEqual(str(product), 'iq mobile - Rs.30000')
        print('isinstance: ', isinstance(product, Product))
        self.assertTrue(isinstance(product, Product))
