
def problem_3():
    filenames = ['cats.txt', 'dogs.txt']
    for filename in filenames:
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            print('That file could not be found.')


problem_3()


def problem_4():
    filenames = ['cats.txt', 'dogs.txt']
    for filename in filenames:
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            pass


problem_4()