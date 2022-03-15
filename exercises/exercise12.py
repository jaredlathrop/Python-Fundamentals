# Problem 1
def problem_1():
    try:
        alpha = input('What is your first number? ')
        beta = input('what is your second number? ')
        alpha = int(alpha)
        beta = int(beta)
        print('The sum of your two numbers is:', alpha + beta)
    except ValueError:
        print('Please input a number.')


# problem_1()


# Problem 2
def problem_2():
    while True:
        alpha = input('What is your first number? ')
        beta = input('what is your second number? ')

        try:
            answer = int(alpha) + int(beta)
            print(answer)
        except ValueError:
            print('Please input a number.')
        else:
            print('')


problem_2()

