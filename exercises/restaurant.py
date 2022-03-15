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