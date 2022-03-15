from users import User


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