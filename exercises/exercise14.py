# problem 1 Page 215 11-1
import unittest


def describe_city(name, country):
    return f'{name}, {country}'


class CitiesTest(unittest.TestCase):
    def test_city_country(self):
        wichita_us = describe_city('wichita', 'united states')
        self.assertEqual(wichita_us, 'wichita, united states')

# Problem 2


def describe_city_2(name, country, population):
    result = f'{name}, {country}'
    if population:
        result += f', {population}'
    return result


class CitiesTest2(unittest.TestCase):
    def test_describe_city_2(self):
        wichita_us_pop = describe_city_2('wichita', 'united states', '500000')
        self.assertEqual(wichita_us_pop, 'wichita, united states, 500000')


# Problem 3
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.lindsay = Employee('lindsay', 'cowin', 50000)

    def test_raise(self):
        self.lindsay.give_raise()
        self.assertEqual(self.lindsay.salary, 55000)

    def test_custom_raise(self):
        self.lindsay.give_raise(10000)
        self.assertEqual(self.lindsay.salary, 60000)


if __name__ == '__main__':
    unittest.main()




# error from problem 2
# FAILED (errors=1)

# Error
# Traceback (most recent call last):
#   File "/Users/jaredlathrop/Python-Fundamentals/exercises/exercise14.py", line 22, in test_city_country2
#     wichita_us_pop = describe_city2('wichita', 'united states', 500000)
# NameError: name 'describe_city2' is not defined

