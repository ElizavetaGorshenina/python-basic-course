class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass_calc(self, unit_mass=25, depth=5):
        return self._length * self._width * unit_mass * depth / 1000


main_road = Road(10000, 5)
print(f'{main_road.asphalt_mass_calc(depth=10)} т')
