# Lesson 10 Encapsulation
# Encapsulation in python is considered weak as it is done by convention
# rather than enforced

# protected members use a single underscore and should not be accessed
# outside-of the class or subclass

class MyClass:
    # protected class variable
    _hi = 'Hello'

    # Constructor
    def __init__(self):
        # Protected instance variable
        self._me = 'World'
        # Private variable
        self.__you = 'You'


# What are properties
# properties allow classes the ability to do things with class variables
# that are either private or protected
# There are 2 different ways, property() and the property decoder
class Feet:
    def __init__(self, length2):
        self._length = length2

    def to_inches(self):
        return self.get_length() * 12

    # getter
    def get_length(self):
        return self._length

    # setter
    def set_length(self, value):
        self._length = value

    # deleter
    def del_length(self):
        del self._length

    # creating the property
    length = property(get_length, set_length, del_length)


# measure = Feet(4)
# print(measure.length)
# print(measure.to_inches())
# measure.length = 6
# print(measure.length)
# print(measure.to_inches())

# the property decorator annotation allows the creation of methods to replace the
# need for the property method


class Centimeter:
    def __init__(self, size):
        self._size = size

    def to_millimeters(self):
        return self._size * 10

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


my_cent = Centimeter(3)
print(my_cent.size)
my_cent.size = 5
print(my_cent.to_millimeters())

# The main function
# if __name__ == '__main__':
    # obj2 = MyClass()
    # print(obj2._hi)
    # Trying to access private variable will result in an error
    # measure = Feet(3)

    # get the length attribute
    # print(measure.length)

    # get the to_inches method result
    # print(measure.to_inches())

    # assign a new value to length
    # measure.length = 5

    # get the to_inches for the new value
    # print(measure.to_inches())


# The property() function.
# the property function is designed to create a property of a class.


