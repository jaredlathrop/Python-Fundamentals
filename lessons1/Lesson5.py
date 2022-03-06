# Arithmetic Operators
# - Follow Pemdas. %
# - add, subtract, multiply, divide (+, -, *, /)
# - Another one is modulus, modulus represents the remainder left over from a division problem
# - another one is exponentiation. The first value is raised to the power of the second value
# - floor division divides and returns the int value and dumps any digit after the example.

# addition example
def add_example():
    result = 10 + 5
    print(result)


# Subtraction example
def sub_example():
    result = 23 - 4
    print(result)


# sub_example()
# add_example()

# Multiplication and Division
def multi_divide(sum1, sum2):
    result_multi = sum1 * sum2
    result_divide = sum1 / sum2
    print(result_multi)
    print(result_divide)


# multi_divide(10, 5)

# modulus example
# result is 21 because the remainder is 21.
def modulus_example(value):
    result_modulus = value % 24
    print(result_modulus)


# Exponentiation example
def exponent_example(value):
    result_exponent = value ** 3
    print(result_exponent)


# modulus_example(189)
# exponent_example(3)
able = 10
beta = 765
# floor division

# result is 76 because it cuts off anything to the right of decimal


def floor_example():
    result_floor = beta // able
    print(result_floor)


# floor_example()


# assignment operators
# - these operators assign a variable to a value, the = we have been using
#   is an operator

def basic_assign(value1, value2):
    value1 += value2
    print(value1)
    value1 -= value2
    print(value1)
    value2 *= value1
    print(value2)
    value2 /= value1
    print(value2)


# basic_assign(5, 3)

def basic_assign2(value):
    value %= 32
    print(value)
    value **= 5
    print(value)
    value //= 8
    print(value)


# basic_assign2(543)


# comparison operators
# - are used for comparing 2 values. the result will either be T/F
# - these are commonly used in conditional statements

# equal and not equal
def compare_two(value1, value2):
    # compares to see if both are equal
    result_equal = value1 == value2
    # compares to see if not equal
    result_not = value1 != value2
    print(result_equal)
    print(result_not)


# compare_two(8, 5)

delta = 10
echo = 34

# greater/less than

def great_less():
    result1 = delta < echo
    result2 = delta > echo
    print(result1)
    print(result2)


# great_less()

# Greater than less than or equal to
def great_less_equal(num1):
    result_great = delta >= num1
    result_less = echo <= num1
    print(result_less)
    print(result_great)


# great_less_equal(10)


# What are logical operators?
# - allow you to combine two comparison operators into one statement
# - very useful in conditional statements

# and example
# result will be false because delta is less than 29.
def logical_and():
    result = echo > 25 and delta > 29
    print(result)


# logical_and()


# or example
def logical_or(num):
    result = echo > num or num < delta
    print(result)


# logical_or(35)


# not example
def logical_not(num1, num2):
    result1 = not(num1 > num2)
    result2 = not(num1 < echo or num2 > delta)
    print(result1)
    print(result2)


# logical_not(5, 35)


# Identity Operators
# - These are used for comparing to see if they are the same object with
#   same memory

def identity_is_not(arg1, arg2, arg3):
    # is
    result1 = arg1 is arg2
    print(result1)
    result2 = arg1 is arg3
    print(result2)
    # is not
    result3 = arg2 is not arg3
    print(result3)


# identity_is_not(5, 10, 5)


# Membership operators
# - These operators are used to test if a sequence is in an object
# - This sequence can be in a list, string, or tuple. It acts likes a search feature.
kilo = "Some kind of words to search through"


# in & not in
def member_in(arg):
    result = arg in kilo
    print(result)
    result = arg not in kilo
    print(result)


member_in('kind')





