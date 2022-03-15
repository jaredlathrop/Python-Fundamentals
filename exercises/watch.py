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