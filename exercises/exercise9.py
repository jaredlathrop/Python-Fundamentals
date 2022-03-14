# Problem 1 8-3, 8-4, 8-5
# 8-3
def make_shirt(size, message):
    print(f'This will be a {size} t-shirt.')
    print(f'It will say, {message}')


# make_shirt('medium', 'NYC!')
# make_shirt(size='medium', message='NYC!')


# 8-4
def make_shirt_2(size='large', message='I love Python'):
    print(f'This will be a {size} t-shirt.')
    print(f'It will say, {message}')


# make_shirt_2()
# make_shirt_2(size='medium')
# make_shirt_2(size='XX large', message='I love C+')

# 8-5
def describe_city(name, country='The United States'):
    message = f"{name} is in {country}."
    print(message)


describe_city('Wichita')
describe_city('Derby')
describe_city('Mexico City', country='Mexico')


# Problem 2, 8-9, 8-10, 8-11.

# 8-9
def show_messages(message):
    print('All messages:')
    for messages in message:
        print(messages)


message = ['hey', 'what\'s up?', 'what are you doing?']
show_messages(message)


# 8-10/8-11
def send_messages(message, sent_message):
    print('Sending all messages:')
    while message:
        current_message = message.pop()
        print(current_message)
        sent_message.append(current_message)


show_messages(message)
sent_message = []
send_messages(message, sent_message)

print('final lists:')
print('to be sent: ', message)
print('has been sent: ', sent_message)


# problem 3 pg 162 9-1 - 9-11
# 9-1
class Restaurant:
    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type
        self.served = 0

    def describe_restaurant(self):
        msg1 = f'{self.restaurant_name} serves {self.food_type}.'
        print(msg1)

    def open_restaurant(self):
        msg2 = f'{self.restaurant_name} is open!'
        print(msg2)

    # 9-4
    def number_served(self, served=0):
        self.served = served
        print('People served: ', served)

    def set_number_served(self, served):
        self.served = served
        print('People served: ', served)

    def increment_number_served(self, add_served):
        self.served += add_served
        print('People served ', add_served)


restaurant = Restaurant('Subway', 'sandwiches')
restaurant.describe_restaurant()
restaurant.open_restaurant()
# part of 9-4
restaurant.number_served()
restaurant.set_number_served(15)
restaurant.increment_number_served(50)


# 9-2
restaurant_1 = Restaurant('Pizza Johns', 'pizza')
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('Mcdonalds', 'fast food')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('Taco Bell', 'fake mexican food')
restaurant_3.describe_restaurant()


# 9-3
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.city = city.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is from {self.city}, and is {self.age} years old!')

    def greet_user(self):
        print(f'It is nice to meet you {self.first_name} {self.last_name}!')

    # 9-5
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


lindsay = User('lindsay', 'cowin', 22, 'wichita')
lindsay.describe_user()
lindsay.greet_user()
# 9-5
lindsay.increment_login_attempts()
lindsay.increment_login_attempts()
lindsay.increment_login_attempts()
print(f'Login attempts: ', {lindsay.login_attempts})
lindsay.reset_login_attempts()
print(f'Resetting log in attempts; Login attempts: ', {lindsay.reset_login_attempts()})

shannon = User('shannon', 'harris', 55, 'wichita')
shannon.describe_user()
shannon.greet_user()

kirk = User('kirk', 'lathrop', 55, 'wichita')
kirk.describe_user()
kirk.greet_user()

# 9-4 is with problem 9-1
# 9-5 is with problem 9-3










