# Looping Statements

# While loop - executes a set of other statements under certain conditions
# You must increment the variable or else the loop will run forever.
# it will run until there is a false condition.

def basic_while(arg):
    alpha = arg
    while alpha <= 4:
        print(alpha)
        # increment by one
        alpha += 1


# basic_while(1)

# For loop
# Executes statements as it iterates a collection or sequence
# You use the keywords for and in as part of the statement followed by a colon
# Collections will be covered later, so we will use a string.

def basic_for(arg):
    for alpha in arg:
        print(alpha)


# basic_for('I like birds')

# Nested loops
# it is possible to have a loop in another loop. Each loop must have its own
# defined variable. The inner loop can use the outer loop variable within itself.

def basic_nested():
    for hop in range(1, 11):
        for bop in range(hop):
            print(hop, end=' ')
        print()
    print()


# basic_nested()


# What is range()
# Used range in the one above, shows a sequence of numbers
# single argument
def basic_single():
    for able in range(5):
        print(able)


# two arguments
def basic_double():
    for beta in range(2, 10):
        print(beta)


def basic_triple():
    for charlie in range(2, 10, 2):
        print(charlie)


# basic_single()
# basic_double()
# basic_triple()

# The pass statement
# The for loops can not be empty. The pass statement will allow you to have a for loop with
# no content.
for num in 'Hello':
    pass


# The break statement
# The break statement is used to stop a loop, it is used in conjunction with an if statement
def basic_break(num1):
    while num1 < 10:
        print(num1)
        if num1 == 5:
            break
        num1 += 1


# basic_break(1)


# using a for loop
def basic_break_for():
    for value in 'Python':
        if value == 'n':
            break
        print(value)


# basic_break_for()


# continue statement will stop an active iteration and begin the next one.
# used with for and while loops. Very similar to break

# This example will skip over the h and print Pyton
def basic_continue():
    for value in 'Python':
        if value == 'h':
            continue
        print(value)


# basic_continue()


# else in loops.
# When the condition is no longer true, the else statement will do something.

def basic_else():
    thing1 = 0
    while thing1 < 4:
        print(thing1)
        thing1 += 1
    else:
        print('loop ends')


basic_else()