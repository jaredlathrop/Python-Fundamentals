# Problem 1 Pg 89 5-8
names = ['admin', 'jamie', 'lindsay', 'shannon', 'trevor']


def problem_1():
    for subject in names:
        if subject == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {subject}, you may not see the status report!')


problem_1()


# problem_1_1 is the second part of problem 1, or 5-9
def problem_1_1():
    names.clear()
    if names:
        for subject in names:
            if subject == 'admin':
                print('Hello admin, would you like to see a status report?')
            else:
                print(f'Hello {subject}, you may not see the status report!')
    else:
        print('There are no users')


problem_1_1()


# Problem 2 Pg 89 5-10
current_users = ['jared', 'lindsay', 'trevor', 'kirk', 'shannon']
new_users = ['david', 'lindsay', 'zoey', 'kirk', 'whitney']


def problem_2():
    for new in new_users:
        if new.lower() in current_users:
            print(f'Sorry {new}, try picking a different name')
        else:
            print(f'{new} is still available')


problem_2()


# problem 3 pg 89 5-11
def problem_3():
    ordinal_numbers = list(range(1, 10))
    for value in ordinal_numbers:
        if value == 1:
            print('1st')
        elif value == 2:
            print('2nd')
        elif value == 3:
            print('3rd')
        else:
            print(f'{value}th')

problem_3()

# problem 4 pg 99 6-1
def problem_4():
    shannon = {
        'first_name': 'shannon',
        'last_name': 'harris',
        'age': '50',
        'city': 'wichita',
    }
    print('first name - ', shannon['first_name'])
    print('last name - ', shannon['last_name'])
    print('age - ', shannon['age'])
    print('city - ', shannon['city'])


problem_4()


# problem 5 pg 112 6-7
people = []
person = {
    'first_name': 'shannon',
    'last_name': 'harris',
    'age': '50',
    'city': 'wichita',
    }
people.append(person)
person = {
    'first_name': 'david',
    'last_name': 'harris',
    'age': '60',
    'city': 'maize',
    }
people.append(person)
person = {
    'first_name': 'kirk',
    'last_name': 'lathrop',
    'age': '50',
    'city': 'derby',
    }
people.append(person)

for person in people:
    name = f"{person['first_name']}, {person['last_name']}"
    age = person['age']
    city = person['city']

    print(f'{name}, of {city}, is {age} years old')












