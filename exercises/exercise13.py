# Problem 1 8-15 thru 8-17
# 8-15
import printing_functions
unprinted_designs = ['dog', 'cat', 'wolf']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8-16/8-17 (the styling is 8/1i7)
# importing basic_function
import basic_function
basic_function.hello_world()
# importing the function hello_world from basic_function

from basic_function import hello_world
print(hello_world())
# importing the function hello_ world andn giving it the alias hw from the
# basic function

from basic_function import hello_world as hw
print(hw())
# importing the basic_function module and giving it the alias bf

import basic_function as bf
bf.hello_world()
# importing all functions from the module basic_function

from basic_function import*
print(hello_world())


# Problem 2
# 9-10
from restaurant import Restaurant
dairy_queen = Restaurant('Dairy Queen', 'Ice Cream')
dairy_queen.open_restaurant()

#9-11
from admin import Admin
lindsay = Admin('Lindsay', 'Cowin', 22, 'Wichita')
lindsay.show_privileges()

#9-12
from admin_privileges import Admin
david = Admin('David', 'Harris', '60', 'Wichita')
david.show_privileges()

# problem 3
# for 9-16 I read about the first one that popped up, string text constants and templates
# The string module dates from the earliest versions of python.