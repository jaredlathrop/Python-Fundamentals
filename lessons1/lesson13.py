# What are modules?
# In their basic form, modules are just python files.
# we use modules to help break up large programs

# Import Statements
# WE use import statements to add modules to our python file
# when we use a direct import statement followed by the name of the ifle
# we import it as a namespace

# please see happy.py for this part

# import happy

# print(happy.express())

# Using from
# you can specify a field or function directly from an import
# using the from keyword with our import.

# using as
# using as keyord allows us to have an alisa to a module

import happy as hey
from math import pi
import house

print(hey.express(False))
print('the value for pi is {0}.'.format(pi))

if __name__ == '__main__':
    house2 = house.House(21, 'dirt', 'straw', 'blue')
    print(house2.door_open_close())

house3 = house.House(27, 'wood', 'bamboo', 'green')
print(house3.door_color)


