# Inheritance and polymorphism
# Inheritance in Python is about objects acquiring all the properties
# and behaviors of a parent object
class Parent:
    # constructor
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def to_name(self):
        return self.name

    def my_eye_color(self):
        return self.eye_color

    def is_working(self):
        return True


class Child(Parent):

    def is_working(self):
        return False


# Parent
my_parent = Parent('James', 'blue')
print(my_parent.name)
print(my_parent.eye_color)
print(my_parent.is_working())

# Child
my_child = Child('David', 'green')
print(my_child.name)
print(my_child.eye_color)
print(my_child.is_working())


class SecondParent:
    def __init__(self, last_name, hair_color):
        self._last_name = last_name
        self._hair_color = hair_color

    def to_last(self):
        return self._last_name

    def is_working(self):
        return True

class SecondChild(Parent, SecondParent):
    def __init__(self, name, last_name, eye_color, hair_color):
        Parent.__init__(self, name, eye_color)
        SecondParent.__init__(self, last_name, hair_color)

    def is_working(self):
        return False


# printing 2nd parent
my_2nd_parent = SecondParent('Smith', 'blonde')
print(my_2nd_parent.to_last())
print(my_2nd_parent.is_working())

# Second child is of both parents
my_2nd_child = SecondChild('Mary', 'Smith', 'blue', 'blonde')
print(my_2nd_child.eye_color)
print(my_2nd_child.is_working())


# Polymorphism using 2 different classes
class Car:
    # constructor
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(str.format('I like my {0} {1}', self._color, self._model))

    def move(self):
        print('My {0} rides fast on the road!'.format(self._model))


class Boat:
    # constructor
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(str.format('I like my {0} {1}', self._color, self._model))

    def move(self):
        print('My {0} rides fast on the water!'.format(self._model))


car_1 = Car('Camaro', 'red')
boat_1 = Boat('Bass Tracker', 'blue')

for vehicles in (car_1, boat_1):
    vehicles.info()
    vehicles.move()


# Polymorphism is Inheritance
class Animal:
    # constructor
    def __init__(self, family):
        self._family = family

    def info(self):
        pass

    def make_sound(self):
        return 'RUMBLE goes the {}'.format(self._family)

    def __str__(self):
        return self._family


class Dog(Animal):
    # constructor
    def __init__(self, name):
        super().__init__('canine')
        self._name = name

    def info(self):
        return 'My dog\'s name is {0} and he is an {1}'.format(self._name, self._family)

    def make_sound(self):
        return 'barks'

    def __str__(self):
        return self._name


class Frog(Animal):
    def __init__(self, name):
        super().__init__('amphibian')
        self._name = name

    def info(self):
        return 'My frog\'s name is {0} and he is a {1}'.format(self._name, self._family)

    def __str__(self):
        return self._name


dog1 = Dog('Lucky')
frog1 = Frog('George')
print(dog1.info())
print(frog1.info())
print(dog1.make_sound())

