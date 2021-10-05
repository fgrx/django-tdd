from django.test import TestCase 

from app.calc import add,sub

class CalcTests (TestCase):
    def test_add_numbers(self):
        """test add numbers"""
        self.assertEqual(add(1,2),3)

    def test_substract_numbers(self):
        """substract_numbers"""
        self.assertEqual(sub(12,7),5)