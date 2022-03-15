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