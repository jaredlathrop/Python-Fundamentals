# problem 1 page 29
# 2-8
print(5+3)
print(9-1)
print(16/2)
print(4*2)
# 2-9
favorite_number = 22
message_1 = "My name is Jared, and my favorite number is {}!"
print(message_1.format(favorite_number))

# Problem 2


def number_sets():
    print(456_234)
    print(68_423_791)
    print(13_794_628)
    print(96_374)


number_sets()

# Problem 3


def two_arguments():
    arg1 = float(1)
    arg2 = int(11.2)
    while arg1 <= 10:
        print(arg1)
        arg1 += 1
    else:
        print('The next number would be {}'.format(arg2))


two_arguments()

# Problem 4


def two_inputs():
    favorite_movie = input('What is your favorite movie?')
    many_times = input('How many times have you seen it?')
    many_times = int(many_times)

    print('I have seen {0} {1} times'.format(favorite_movie, many_times))


two_inputs()


