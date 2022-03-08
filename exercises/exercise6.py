# Problem 1
# On page 84 of your book, do 5-3 of the try it yourself.
alien_color = 'green'


def problem_1():
    if 'green' in alien_color:
        print('You have earned 5 points because the alien\'s color is green!')
# Write one version of this test that passes and one that fails.
    if 'yellow' in alien_color:
        print('This is the version that passes!')
    if 'blue' in alien_color:
        print('This will have no output but it is for the sake of the assignment.')


problem_1()


# Problem 2
def problem_2():
    if 'green' in alien_color:
        print('You have earned 5 points for shooting the green alien!')
    if 'yellow' != alien_color:
        print('The alien you shot wasn\'t green, you have earned 10 points!')
    else:
        print('This is to satisfy the 2nd part of the problem')


problem_2()


# problem 3
def problem_3():
    alien_color_1 = 'green'
    if 'green' in alien_color_1:
        print('You have earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You have earned 10 points for shooting the yellow alien!')
    elif 'red' in alien_color_1:
        print('You have earned 15 points for shooting the red alien!')


problem_3()


def problem_3_1():
    alien_color_1 = 'yellow'
    if 'green' in alien_color_1:
        print('You have earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You have earned 10 points for shooting the yellow alien!')
    elif 'red' in alien_color_1:
        print('You have earned 15 points for shooting the red alien!')


problem_3_1()


def problem_3_2():
    alien_color_1 = 'red'
    if 'green' in alien_color_1:
        print('You have earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You have earned 10 points for shooting the yellow alien!')
    elif 'red' in alien_color_1:
        print('You have earned 15 points for shooting the red alien!')


problem_3_2()

# Problem 4


def problem_4():
    age = 15
    if age < 2:
        print('You are a baby!')
    elif 2 <= age < 4:
        print('You are a toddler!')
    elif 3 <= age < 13:
        print('You are a kid!')
    elif 13 <= age < 20:
        print('You are a teenager!')
    elif 20 <= age < 65:
        print('You are an adult!')
    else:
        print('You are an elder!')


problem_4()


# Problem 5
def check_if_bool(arg):
    print(bool(arg))


check_if_bool('dog')
# The integer 5 printed true
# 0 printed false
# dog printed true

