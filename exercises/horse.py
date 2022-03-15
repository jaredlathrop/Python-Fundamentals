class Horse:
    def __init__(self, horse_weight, horse_height, horse_sex, horse_color):
        self._horse_weight = horse_weight
        self._horse_height = horse_height
        self._horse_sex = horse_sex
        self._horse_color = horse_color

    @property
    def horse_weight(self):
        return self._horse_weight

    @horse_weight.setter
    def horse_weight(self, value):
        self._horse_weight = value

    @property
    def horse_height(self):
        return self._horse_height

    @horse_height.setter
    def horse_height(self, value):
        self._horse_height = value

    @property
    def horse_sex(self):
        return self._horse_sex

    @horse_sex.setter
    def horse_sex(self, sex):
        self._horse_sex = sex

    @property
    def horse_color(self):
        return self._horse_color

    @horse_color.setter
    def horse_color(self, color):
        self._horse_color = color


my_horse = Horse(500, 60, 'Male', 'brown')
print('Here is my horse!')
print('The horse weighs', my_horse.horse_weight, 'pounds!')
print('The horse is', my_horse.horse_height, 'inches tall!')
print('The horse is a', my_horse.horse_sex)
print('The horse is', my_horse.horse_color)

