# Classes and functions

# Basic class definition
# classes are capitalized
class Cat:
    # class variable
    kind = 'feline'

    # constructor
    def __init__(self, name, color):
        # instance variables
        self.name = name
        self.color = color

    # basic method
    def cat_color(self):
        return self.color

    def cat_name(self):
        return self.name


# object creation
my_cat = Cat('Felix', 'brown')
my_cat_2 = Cat('Garfield', 'orange')

# name is unique to the created object
# Here are some print examples
# print(my_cat.cat_name())
# print(my_cat_2.kind)
# print(my_cat_2.cat_color())


# Functions review
# keyword argument allows you to change the order of the function paramenters
# when calling that method
def my_fancy_function(arg1, arg2):
    print(arg1 + ' ' + arg2)


# my_fancy_function('hey', 'viewer')
# my_fancy_function(arg2='weekend', arg1='Saturday')


# arbitrary arguments allow for many arguments that are unknown
# using *args and **kwargs will help define these arguments


# *args will allow a tuple of arguments
def favorite_color(*colors):
    print('my favorite color is ' + colors[1])


# favorite_color('brown', 'red', 'blue')

# using **kwargs will allow a dictionary of arguments
def vehicles(**truck):
    print('My truck is a ' + truck['model'])


# vehicles(make='Chevy', model='Silverado')


# Using the default argument allows you to have more than one, with one
# given a default value. These defaults come after other arguments
def my_hello(arg, arg2='hi'):
    print(arg2 + ' ' + arg)


# my_hello('Tom')
# my_hello('Tim', 'Hello')


# using a return keyword will return the value back out of the funciton
# to a variable you define to the left of the function
def simple_add(value1, value2):
    return value1 + value2


# total = simple_add(12, 23)
# print(total)
# print(simple_add(5, 10))


# Main function is what is called when a python file is ran through the compiler
# it will perform all actions in the file except functions unless they
# are called directly

if __name__ == '__main__':
    total = simple_add(12, 23)
    print(total)



