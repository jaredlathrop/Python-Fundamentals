# Boat
class Boat:
    def __init__(self, hull_shape, sail, wood_type, captain):
        self._hull_shape = hull_shape
        self._sail_type = sail
        self._wood_type = wood_type
        self._captain_name = captain

    @property
    def hull_shape(self):
        return self._hull_shape

    @hull_shape.setter
    def hull_shape(self, shape):
        self._hull_shape = shape

    @property
    def sail_type(self):
        return self._sail_type

    @sail_type.setter
    def sail_type(self, type):
        self._sail_type = type

    @property
    def wood_type(self):
        return self._wood_type

    @wood_type.setter
    def wood_type(self, wood):
        self._wood_type = wood

    @property
    def captain_name(self):
        return self._captain_name

    @captain_name.setter
    def captain_name(self, name):
        self._captain_name = name


my_boat = Boat('V-Shape', 'cloth', 'oak wood', 'Captain Jeremy')
print('Here is my boat!')
print('The captain is:', my_boat.captain_name)
print('The sail is made of:', my_boat.sail_type)
print('The wood used is:', my_boat.wood_type)
print('The hull shape is:', my_boat.hull_shape)


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


class Watch:
    def __init__(self, watch_weight, watch_hands, watch_material, watch_color):
        self._watch_weight = watch_weight
        self._watch_hands = watch_hands
        self._watch_material = watch_material
        self._watch_color = watch_color

    @property
    def watch_weight(self):
        return self._watch_weight

    @watch_weight.setter
    def watch_weight(self, value):
        self._watch_weight = value

    @property
    def watch_hands(self):
        return self._watch_hands

    @watch_hands.setter
    def watch_hands(self, num):
        self._watch_hands = num

    @property
    def watch_material(self):
        return self._watch_material

    @watch_material.setter
    def watch_material(self, material):
        self._watch_material = material

    @property
    def watch_color(self):
        return self._watch_color

    @watch_color.setter
    def watch_color(self, color):
        self._watch_color = color


my_watch = Watch(10, 2, 'gold', 'gold')
print('Here is my watch!')
print('The watch weighs', my_watch.watch_weight, 'ounces')
print('The watch has', my_watch.watch_hands, 'hands')
print('The watch is made of', my_watch.watch_material)
print('The watch is', my_watch.watch_color, 'colored')


class Guitar:
    def __init__(self, string_number, string_length, guitar_type, guitar_wood_type):
        self._string_number = string_number
        self._string_length = string_length
        self._guitar_type = guitar_type
        self._guitar_wood_type = guitar_wood_type

    @property
    def string_number(self):
        return self._string_number

    @string_number.setter
    def string_number(self, value):
        self._string_number = value

    @property
    def string_length(self):
        return self._string_length

    @string_length.setter
    def string_length(self, value):
        self._string_length = value

    @property
    def guitar_type(self):
        return self._guitar_type

    @guitar_type.setter
    def guitar_type(self, type):
        self._guitar_type = type

    @property
    def guitar_wood_type(self):
        return self._guitar_wood_type

    @guitar_wood_type.setter
    def guitar_wood_type(self, wood):
        self._guitar_wood_type = wood


my_guitar = Guitar(8, 26, 'acoustic', 'oak')
print('Here is my Guitar!')
print('The guitar has', my_guitar.string_number, 'strings!')
print('The guitar\'s strings are', my_guitar.string_length, 'inches long!')
print('This is an', my_guitar.guitar_type, 'guitar!')
print('The guitar is made of', my_guitar.guitar_wood_type, 'wood!')
