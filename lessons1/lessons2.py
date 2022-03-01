# My Application Overview Lesson

# This function should be lowercase, and if more than one word
# it should have an underscore to separate each word.
# a parenthesis after the name should be followed by a colon
# statements that are part of a function should be 4 spaces indented

def my_function():
    print('Hello')
    print('World')
# to run the function you must call it by name


my_function()


# When defining a function with arguments, those are arguments go in between
# The parenthesis and separated by comma
def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other('Red', 'Green')


# Variable names
# - must start with a letter or and underscore, they cant begin with numbers
# - can only contain numbers, letters, or underscores
# - VARIABLES ARE CASE SENSITIVE
# - the variable on the left while the literal is on the right
# - a combined variable and literal is a field
value = 'Blue'
value2 = 10
print(value)
print(value2)

# Variables can even change types, although you may want to avoid this
value3 = "Happy"
print(value3)
value3 = 20
print(value3)


# Multi-line statements use a backslash to continue a statement on a second line
alpha = 1 + 2 + 3\
    + 4 + 5
print(alpha)

# more than 1 variable on the same line - I don't like the look of this lol.
beta = 10; charlie = "python"; delta = 5
up, down, left = "town", "stairs", "right"
print(up)
print(down)
print(left)


# classes in python
# - a class variable is a variable that is shared by all instances
#   of the object, these could be considered attributes
# - functions for the class are also defined and any variable
#   created in that method is an instance variable.
# - A class is created using the keyword class followed by the class name
# - A class is an object
# - I need to leave 2 empty lines after class is defined
# - Basic class example:
class MyFirstClass:
    name = 'Jared'

    def something(self):
        print('something')


my_class = MyFirstClass()
print(my_class.name)
my_class.something()







