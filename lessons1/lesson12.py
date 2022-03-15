# Exception Handling

def simple_divide():
    print('Let\'s divide two numbers.')
    try:
        first = input('The first number is: ')
        second = input('the second number is: ')
        answer = int(first) / int(second)
        print(answer)
    except (ZeroDivisionError, ValueError):
        print('you can\'t divide by zero, or use a string.')


# simple_divide()

# What is the Try Block
# The try block contains a set of statements where an exception could oocur
# What is the else block?
# The else block is written after the except. This block is where you put code
# that does not need to be put in the try. IF the try block succeeds, the else block will execute
# if the try block fails, teh code in the else blcok will not execute


def multi_except_sample():
    names = ('Dave', 'Matt', 'Jody')
    these = (25.4, 30j, 34)

    try:
        delta = int(these[3])
        echo = complex(these[0], 5)
        print('Delta is ' + str(delta))
    except IndexError:
        print('Please provide at lease 1 argument.')
    except ValueError:
        print('That is not a number!')
    except TypeError:
        print('You have provided something that is odd.')
    except NameError:
        print('I don\'t know how to calculate that')


# multi_except_sample()


alpha, fox = 5, 10


def sample_except_else(arg):
    try:
        if fox > arg:
            golf = fox / arg
            print('value is {0}'.format(golf))
    except ZeroDivisionError:
        print('an error has occurred')
    else:
        print('Division was successful')


# sample_except_else(0)


# The Finally Block
# the Finally Block is the last block that will be defined
# This block is executed regardless of whether the try block succeeds

def sample_finally():
    try:
        if fox > alpha:
            bravo = fox / (fox - alpha) - 5
            charlie = fox / 0
            print('Value is {0}'.format(bravo))
            print('try prints')
    except ZeroDivisionError:
        print('an error occurred')
        print('Zero division error occurred')
    else:
        print('else prints')
    finally:
        print('finally prints')


sample_finally()
