# What are strings
# - A String is a sequence of characters between single or double
#   quotes
# - single quotes, I prefer singles. Here's an example:

alpha = 'Hello'
beta = 'Python'
# print results
print(alpha)
print(beta)

# - A Multi-line string uses 3 single or three double quotes and allows
#   a string to be created on multiple lines, Example:
multi = '''this string can be seen
on multiple lines so you could do
paragraphs if you wanted'''
print(multi)

# slice syntax
# - gives you a range of characters from a start and end positions
# - can be separated with a colon

# - getting a specific index using the square bracket[]
charlie = 'Happy'
print(charlie[2])

# - The output above should be P
# - If you put in a value of the index that is higher than
#   the number of characters -1 you will generate an error
# - It starts counting at 0, so the example above would have characters
#   0-4

# - slicing and range of characters
# - using the same square brackets, you can output a range of characters
#   from a string. this is called slicing, you use a colon to separate
#   the start and end of the slicing
delta = 'enjoy python'
print(delta[2:5])
# - this example will print a range of characters, this specific output will be joy

# - negative slicing uses negative numbers. instead of starting from 0,
#   it begins at the end of the string
#   - here's an example
print(delta[-5:-2])
# output should be yth


# What is Check String?
# - check string is the ability to see if a certain phase of character
#    in a string. there are 2 keywords that define this in/not in. the result will be either T/F.

txt = 'this is a test sentence'
result1 = 'is' in txt
# There is a 'is' so will print true.

# using the not in keyword
txt2 = 'this other phrase is also a test'
result2 = 'th' not in txt2
# there is a th so will print False

# testing the results.
print(result1)
print(result2)

# String Concatenation
# - the joining of string literals or defined variables using the + operator
# - The original strings are not changed, a new string literal is created once the
#   concatenation has finished
cat1 = 'Happy'
cat2 = 'Friday'
combine = cat1 + cat2
print(combine)
# output will be HappyFriday
combine2 = cat1 + " " + cat2
print(combine2)
# this is how to add a space
# Output is Happy Friday

cat3 = 'Sample'
combine3 = cat3 + ' Code'
print(combine3)
# The one above is concatenation with a literal instead of 2 variables.

# long concatenation with more than 2 values
combine4 = cat1 + ' ' + cat2 + ' ' + combine3
print(combine4)

# What is string format?
# String format is a method that allows strings and numeric data types to be combined
# like string concatenation. string format utilizes curly braces {} to act as placeholders

# basic string format using only a curly brace
age = 4
msg1 = 'my dog is {} years old'
print(msg1.format(age))
# this will pring my dog is 4 years old

# string format using indexing
msg2 = 'my dog {1} is {0} years old'
print(msg2.format(age, 'Spot'))
# this will print my dog Spot is 4 years old

# optional format
name = 'John'
total = 34.9856

msg3 = 'Hello, {0} your total is {1:5.2f}'
print(msg3.format(name, total))
# 1:5 is indexing from earlier.

# escape sequences
# octal escape sequence '\110\145\154\154\157
value_0 = '\110\145\154\154\157'
print(value_0)

# Escape Sequence allows you to use characters that are reserved using a
# backslash \
# In the example below we use 3 examples of escape sequences
# \t is tab, \n is new line, \' allows me to use the "'"
value_more = 'That\'s a cool toy. \tCan I\n play with it'
print(value_more)

# String Methods - Methods are an organized way to complete an action done at the object level.
#  String methods are methods built into python
value_string = ' Hello, World '
# Strip() - strips the white space
print(value_string.strip())

# lower() - makes lower case
print(value_string.lower())

# upper() - makes upper case
print(value_string.upper())

# replace() - replaces a character
print(value_string.replace('e', 'a'))
# will print Hallo World

# split () - Prints [ ' Hello', ' World ']
print(value_string.split(','))

value_second = 'hello python'
# capitalize()
print(value_second.capitalize())

value_upper = 'PYTHON'

# casefold()
print(value_upper.casefold())

# center() - centers within 40 spaces
print(value_second.center(40))







