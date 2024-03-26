import unittest
'''
class MyClass:
    def __init__(self, x: bool):
        self.x = x

    def my_method(self):
        if self.x:
            return 0
        else:
            return 1

class MyClassTest(unittest.TestCase):
    def test_my_method(self):
        self.assertEqual(0,
                         MyClass(True).my_method())
        self.assertEqual(1,
                         MyClass(False).my_method())

        #AssertionError: 1 != 0
        self.assertEqual(-1,
                         MyClass(False).my_method())

if __name__ == '__main__':
    #Run unit tests
    unittest.main() '''

'''Class MyTestCase(TestCase):
    def test_example(self):
        self.assertEqual(1, 1)
        self.assertAlmostEqual(1.0, 2 / 2)
        self.assertNotEqual(1, 2)
        self.assertTrue(1 == 1)
        self.assertFalse(1 != 1)
        self.assertGreater(2, 1)

        with self.assertRaises(Exception):
            raise Exception('...')'''

print('**************************************************')

class Dish:
    def __init__(self, name: str, price_cent: int):
        if price_cent <= 0:
            raise Exception('Preis muss größer 0 sein!')
        self.name: str = name
        self.price_cent: float = price_cent

    def __eq__(self, other) -> bool:
        return isinstance(other, Dish) and self.name == other.name and \
               self.price_cent == other.price_cent

    def __str__(self) -> str:
        return "{}: {} €".format(self.name, (self.price_cent /100.))

class DishTest(unittest.TestCase):
    #Test1
    def test_init(self):
        dish = Dish('my_dish', 100)
        self.assertEqual(dish.name, 'my_dish')
        self.assertEqual(dish.price_cent, 100)

        with self.assertRaises(Exception):
            Dish('illegal_dish', -1)

    #Test2
    def test_str(self):
        self.assertEqual("my_dish: 1.0 €",
                        str(Dish('my_dish', 100)))
        self.assertEqual("other_dish: 3.99 €",
                        str(Dish('other_dish', 399)))


    #Test 3
    def test_eq(self):
        dish = Dish('my_dish', 100)
        # compare with same instance
        self.assertEqual(dish, dish)
        # compare with equal instance
        self.assertEqual(dish, Dish('my_dish', 100))
        # compare with different instance
        self.assertNotEqual(dish, Dish('other_dish', 200))
        # compare with instance of other class
        self.assertNotEqual(dish, ('my_dish', 100))