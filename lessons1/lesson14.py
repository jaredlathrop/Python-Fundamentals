# Testing your code
# Unit Test
# A unit test checks one aspect of a function's behavior. for each test needing to
# be done on a function call. will require a new unit test.

# a test case is a collection of unit test to ensure a function is tested
# on many situations. Test cases are made up of a class that imports the
# unit test module and subclass the unittest.TestCase class


# define a function that can be tested
import unittest
from house import House

def get_make_model(make, model):
    vehicle_type = '{0} {1}'.format(make, model)
    return vehicle_type


class Sample_Testing(unittest.TestCase):
    # positive passing test
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    # negative failing test
    def test_lower(self):
        self.assertEqual(('hello'.lower(), 'Hello'))

    def test_make_model(self):
        formatted = get_make_model('Chevy', 'Silverado')
        self.assertEqual(formatted, 'Chevy Silverado')


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House(20, 'concrete', 'steel', 'red')

    def test_door_color(self):
        self.assertEqual(self.house.door_color, 'red')

    def test_door_open_close(self):
        self.assertIsNone(self.house.door_open_close())


if __name__ == '__main__':
    unittest.main()

# Testing a class
#

