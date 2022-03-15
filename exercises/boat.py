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