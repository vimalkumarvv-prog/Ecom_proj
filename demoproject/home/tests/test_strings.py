from django.test import TestCase


# Create your tests here.

def demo(text1, text2):
    return text1 + text2


class Testdemo(TestCase):
    def test_concatenate(self):
        self.assertEqual(demo("Saraswathy", " Venu"), "Saraswathy Venu")
