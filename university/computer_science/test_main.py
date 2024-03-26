from unittest import TestCase
from einführung_informatik.main import biggest

class MainTest(TestCase):
    def test_biggest(self):
        #self.fail()
        self.assertEqual(biggest(2,5,3), 5)
        self.assertEqual(biggest(8, 5, 3), 8)
        self.assertEqual(biggest(2, 5, 3), 5)
