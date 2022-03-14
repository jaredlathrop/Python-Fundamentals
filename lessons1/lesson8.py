# The list collection
# List is a type of collection, it is ordered and can be changed. It allows duplicate data
# to define, you use square brackets
# you can have strings and numbers in the lists
# The first member starts at 0 rather than 1

colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
          'white', 'orange']
size = [42, 32, 156, 89, 34, 23, 89]
mixed = [23, 'happy', 'python', 90, 45, 'snow', 'car', 56]


# direct print
def simple_print():
    print(colors)


# simple_print()


# print 1 item in the list
def simple_single_print():
    print(size[3])


# simple_single_print()


# for loop of list
def simple_for_print():
    for mix in mixed:
        print(mix)


# simple_for_print()

# Getting a range of values
# - You can get a range of valies from a list using the colon to seperate the starting
#   and ending values.

def simple_print_range():
    print(colors[2:5])
    print(mixed[1:3])
    print(size[0:3])


# simple_print_range()

# list Length and Item validation
# the len method returns the number of items in the list
# using the 'in' keyword and the if statement, you can quickly search for
# an item
def simple_length():
    my_colors = len(colors)
    print(len(colors))
    value = 0
    while value < my_colors:
        print(colors[value])
        value += 1


# simple_length()

# using in keyword to search a list for the item
def simple_search():
    if 89 in size:
        print('89 is in the size list')
    else:
        print('89 is not in size list')


# simple_search()

# Adding items
# there are two ways to add items to an existing list:
# append and list
# append will insert at the end of the list

def simple_append():
    mixed.append('Friday')
    for mix in mixed:
        print(mix)


# simple_append()

# insert will allow you to insert at a specific index position
def simple_insert():
    mixed.insert(3, 'Friday')
    for value in mixed:
        print(value)


# simple_insert()

# Removing items
# There are several methods for removing items from a list
# - remove(), pop(), del, clear()

# The remove function will remove a specified value
def simple_remove():
    mixed.remove('happy')
    for mix in mixed:
        print(mix)


# simple_remove()


# The pop() function will remove a specified value based on it's index.
def simple_pop():
    mixed.pop(2)
    for mix in mixed:
        print(mix)


# simple_pop()

# Simple del
def simple_del_none():
    trucks = ['chevy', 'ford', 'gmc']
    del trucks
    trucks.append('toyota')
    for value in trucks:
        print(value)
    # Del removes the list entirely...


# simple_del_none()

# Clear method will empty a list, but not remove the list entirely
def simple_clear():
    mixed.clear()
    for mix in mixed:
        print(mix)
    # So we cleared the list above, below we're adding the string lonely to the list.
    mixed.append('lonely')
    print(mixed)


# simple_clear()


# List operations: concatenation, repeat, membership, iterate
# concatenation
def simple_join():
    values1 = [1, 2, 3, 4]
    values2 = [5, 6, 7, 8]
    total = values1 + values2
    for val in total:
        print(val)


# simple_join()

# repeat will repeat a list a certain amount of times
def simple_repeat():
    values = [1, 2, 3, 4]
    print(values * 3)


# simple_repeat()

# membership
def simple_membership():
    result = 'red' in colors
    print(result)


# simple_membership()


# iterate
def simple_iterate():
    for color in colors:
        print(color, end=' ')


# simple_iterate()

# The tuple
# Like the list collection, the tuple collection is ordered. The tuple however is unchangeable
# Which basically means, once you create the list, it can't be changed. That maek the tuple collection immmutable.
# The tuple collection is ap zero indexed.
my_fruits = ('apple', 'banana', 'cherry', 'orange')
# print(my_fruits)


def simple_tuple():
    for fruit in my_fruits:
        print(fruit)

    print(my_fruits[2:4])


# simple_tuple()

# Change a value in a tuple by converting to list and then back again
def simple_change_tuple():
    fruity = list(my_fruits)
    fruity[2] = 'peach'
    my_fruit = tuple(fruity)
    for fruit in my_fruit:
        print(fruit)


# simple_change_tuple()

# Since tuples are unchangeable, there are a few additional things that it can not perform
# The del keyword can only delete the entire tuple
# You can join tuples together using the + operator. You cannot add items once a tuple is created


# The set collection type is both unordered, and it is un-indexed.
ice_cream = {'chocolate', 'vanilla', 'strawberry', 'neopolitan',
             'chocolate chip', 'rocky road', 'cookie dough'}


def simple_set():
    for flavor in ice_cream:
        print(flavor)


# simple_set()


# You can't change an item once in a set, you can continue to add items.
# there are two ways, add and update

def simple_set_add():
    ice_cream.add('bunny tracks')
    for value in ice_cream:
        print(value)


# simple_set_add()
def simple_set_update():
    ice_cream.update({'butter pecan', 'bunny tracks', 'peanut butter cup'})
    for flavor in ice_cream:
        print(flavor)


# simple_set_update():


# removing itmes can be done in 3 ways: remove(), discard(), & pop()
# remove will generate an error if the item being removed does not exist
def simple_set_remove():
    num_windows = {34, 23, 78, 98, 37}
    num_windows.remove(98)
    for num in num_windows:
        print(num)


# simple_set_remove()

def simple_set_discard():
    letters = {'a', 'b', 'c', 'd', 'e'}
    letters.discard('a')
    for letter in letters:
        print(letter)


# simple_set_discard()

# pop will remove the last item from the list, so you don't know what's being removed
def simple_set_pop():
    letters = {'a', 'b', 'c', 'd', 'e'}
    letters.pop()
    for alpha in letters:
        print(alpha)


# simple_set_pop()

# joining set collections by update, union and | operator
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
tens = {10, 20, 30, 40, 50}


# update
def simple_set_join():
    even.update(odd)
    for num in even:
        print(num)


# simple_set_join()


# union
def simple_set_union():
    value = tens.union(odd)
    for items in value:
        print(items)


# simple_set_union()


# | operator
def simple_set_pipe():
    numbers = odd | even | tens
    for val in numbers:
        print(val)


# simple_set_pipe()


# Dictionary Collection
# dictionaries are collections consisting of a key and value
# the key is unique and cannot be duplicated making it immutable
# the value however can be a duplicate

cars = {101: 'acura', 102: 'honda', 103: 'ford'}
# print(cars.get(102))
# adding and changing within dictionary
# cars[104] = 'chevy'
# cars[102] = 'not honda'
# print(cars)


# Looping through a dictionary: basic print
def simple_dict_loop():
    for car in cars:
        print(car)


# this will print all the keys
# simple_dict_loop()


# loop using [ ]
def simple_dict_square():
    for car in cars:
        print(cars[car])


# will print the values not the keys
# simple_dict_square()


# loop using values method
def simple_dict_values():
    for some in cars.values():
        print(some)


# will print values not the keys
# simple_dict_values()


# loop getting both key and value using items() method
def simple_dict_both():
    for able, beta in cars.items():
        print(able, ' - ', beta)


# prints key and value
# simple_dict_both()


# Nested dictionaries
# a dictionary can contain many dictionaries, this is called a nested dictionary
my_pallet = {'color': {'primary': 'red', 'secondary': 'maroon'},
             'color2' : {'primary': 'blue', 'secondary': 'royal'}}


def simple_dict_multi():
    for col1, col2 in my_pallet.items():
        print(col1, ' - ', col2)


# simple_dict_multi()







