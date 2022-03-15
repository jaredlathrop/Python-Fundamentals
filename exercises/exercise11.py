# Problem 1, pg 173 9-6
class Restaurant:
    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type

    def describe_restaurant(self):
        msg1 = f'{self.restaurant_name} serves {self.food_type}.'
        print(msg1)

    def open_restaurant(self):
        msg2 = f'{self.restaurant_name} is open!'
        print(msg2)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, food_type='ice cream'):
        super().__init__(restaurant_name, food_type)
        self.flavors = []

    def show_flavors(self):
        print('We have 3 different flavors available.')
        for flavor in self.flavors:
            print(f'{flavor}')


dairy_queen = IceCreamStand('Dairy Queen')
dairy_queen.flavors = ['chocolate', 'caramel', 'vanilla']
dairy_queen.describe_restaurant()
dairy_queen.show_flavors()


# Problem 2 9-7
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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = []

    def show_privileges(self):
        print('here are your admin privileges')
        for privilege in self.privileges:
            print(f'{privilege}')


lindsay = Admin('Lindsay', 'Cowin', '22', 'Wichita')
lindsay.describe_user()
lindsay.privileges = ['can add post', 'can delete post', 'can ban user']
lindsay.show_privileges()


# 9-8

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(f'{privilege}')
        else:
            print('you have no privileges')


kirk = Admin('Kirk', 'Lathrop', 60, 'Wichita')
kirk_privileges = ['can shut down host', 'can reset username', 'can access settings']
print(kirk_privileges)






