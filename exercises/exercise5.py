# problem 1
phrase = 'This is the test phrase'


def example_1(arg1, arg2, arg3):
    # I will be using 'is' for arg1, 'phrase' for arg 2, and '10' for arg 3
    result = arg1 in phrase
    print('I predict True, here is the result: ', result)
    # I predict this will print false
    result_1 = arg1 not in phrase
    print('I predict False, here is the result: ', result_1)
    # I predict this test will print false because is does not equal the entire variable.
    result_2 = arg1 == phrase
    print('I predict False, here is the result: ', result_2)
    # I predict this test will print true because 'is' is not equal to the variable.
    result_3 = arg1 != phrase
    print('I predict True, here is the result: ', result_3)
    # I predict this test will print true because 'phrase' is in the variable
    result_4 = arg2 in phrase
    print('I predict True, here is the result: ', result_4)
    result_5 = arg2 not in phrase
    print('I predict False, here is the result: ', result_5)
    result_6 = arg2 == phrase
    print('I predict False, here is the result: ', result_6)
    result_7 = arg2 != phrase
    print('I predict True, here is the result: ', result_7)
    result_8 = arg3 != phrase
    print('I predict True, here is the result: ', result_8)
    result_9 = arg3 == phrase
    print('I predict False, here is the result: ', result_9)


example_1('is', 'phrase', 10)


# problem 2
# part 1: testing for equality and inequality
# Tests for equality and inequality
soccer_team = 'Liverpool'
if soccer_team == 'Liverpool':
    print('Go Liverpool!')
if soccer_team != 'Arsenal':
    print('You should really root for Liverpool instead of Arsenal.')

# Tests using the lower method
# True Example
soccer_team2 = 'Chelsea'
soccer_team2.lower == 'Chelsea'
print("This is for the lower method:", soccer_team2 == 'Chelsea')
# False Example
print('This is for the lower method:', soccer_team2 == soccer_team2.lower())

# Numerical tests involving equality, inequality, greater than, less than, greater than or equal to
# and less than or equal to
jared = 23
david = 60
# Equality
result_10 = (jared == david)
print('This is for equality, it should print false:', result_10)
result_11 = (jared != david)
print('This is for inequality, it should print true:', result_11)
# Greater than or less than
result_12 = (jared > david)
print('This is for greater than, it should print false:', result_12)
result_13 = (jared < david)
print('This is for less than, it should print true:', result_13)
# Greater than or equal to/less than or equal to.
result_14 = (jared >= david)
print('This is for greater than or equal to, it should print false:', result_14)
result_15 = (jared <= david)
print('this is for less than or equal to, it should print true:', result_15)

# Using keywords
# or examples
result_16 = jared >= 70 or david >= 70
print('This is my or example, it should print false:', result_16)
result_17 = jared >= 20 and david >= 50
print('This is and example, it should print true:', result_17)

# In a list
english_teams = ['liverpool', 'chelsea', 'arsenal']
# True
print('Is Liverpool an English team? Let us see:', 'liverpool' in english_teams)
# False, (Whether an item is not in a list)
print('Is Barcelona an English team? Let us see:', 'barcelona' in english_teams)


# Question 3


def game_scores(score1, score2):
    result_18 = score1 * score2
    print('Multiplication:', result_18)
    result_19 = score1 / score2
    print('Division:', result_19)
    result_20 = score1 % score2
    print('Modulus:', result_20)
    result_21 = score1 ** score2
    print('Exponential:', result_21)
    result_22 = score1 + score2
    print('Addition:', result_22)
    result_23 = score1 - score2
    print('Subtraction:', result_23)
    result_24 = score1 // score2
    print('Floor division:', result_24)


game_scores(50, 10)


# Question4
def assignment_operator(value):
    # Modulus Equals
    value %= 4
    print('Modulus equals:', value)
    # Exponent Equals
    value **= 5
    print('Exponent equals:', value)
    value += 6
    print('Addition equals:', value)
    value -= 6
    print('Subtraction equals:', value)


assignment_operator(10)











