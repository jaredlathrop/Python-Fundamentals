# What are numeric types
# - 3 different types, int, float, and complex
# - These types can be assigned to a variable in the same way as strings
# - If you need to verify a numeric type, you can call the method type()
# - Int is a whole number that is neg/pos.
# - Float is a number that is neg/pos that contains a decimal, float is accurate up to 15 decimal places
# - Complex is made of real and imaginary parts represented by a formula where a and b
#   are the floats and J or j represents an imaginary number. x=3j, the imaginary part defaults
#  to 0 and only including 0-9 or unicode equivalent the Nd property. This numeric type is not used often.

# int in detail
val_int1 = 42
val_int2 = 8178789
val_int3 = -393939
val_int4 = 1234567802

# print the values
print(val_int4)
print(val_int3)
print(val_int2)
print(val_int1)

# get the type of one of our values above
print(type(val_int4))

# float in detail
val_float1 = 3.14
val_float2 = 2.14848484
val_float3 = 15.3333333
val_float4 = -19.4

# print the values
print(val_float4)
print(val_float3)
print(val_float2)
print(val_float1)

# print the type of the float values
print(type(val_float4))

# scientific notation
val_float5 = 25e4
val_float6 = 42e9
val_float7 = -98.6e2

# print them
print(val_float5)
print(val_float6)
print(val_float7)

# complex in partial detail
val_complex1 = 3j
val_complex2 = -5j

print(val_complex1)

# what is the numeric system
# - numbers can be represented in different ways. we typically deal with numbers
#   that are called decimal, or base10. Not to be confused with int or float,
#   the decimal represents the system rather than the type. Base10, means the numbers consist
#   0-9.
# - There are other numeric systems such as binary, octal and hexadecimal,
# - you can utilize the methods of bin(), oct(), & hex() to return the numeric system
#   values from int values. These methods do not work for float or complex.
# - below are examples of using bin(), oct(), & hex() to return the numeric system values
#   from int values

print(bin(42))
print(oct(42))
print(hex(42))

# type conversion
# some situations, you need to convert one data type to another
# each type has a method that will allow you to do these conversions

value = 0b10110
print(value)

# taking values that are strings and converting, while also converting numbers
# to strings
value1 = float(34)
value2 = int(34.5)
value3 = str('89.3')
value4 = str('48')
value5 = int('45')
value6 = float('23.5')

# print values used in converting
print(value1)
print(value2)
print(value3)
print(value4)
print(value5)
print(value6)

# Input method
# - allows information to be entered by the user based on a question. this info is treated
#   as a string when it is assigned to a variable
# - Even numbers entered from a user is treated as a string
# name = input('What is your name?')
# height = int(input('what is your height in inches?'))

name = input('what is your name')
movie = input('what is your favorite movie')

message = 'my name is {0} and my favorite movie is {1}'
print(message.format(name, movie))

