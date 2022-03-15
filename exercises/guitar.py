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