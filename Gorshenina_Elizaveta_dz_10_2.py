from abc import ABC, abstractmethod


class Closes(ABC):

    @abstractmethod
    def material_usage_calc(self):
        pass


class Coat(Closes):

    def __init__(self, v):
        self._v = v

    @property
    def material_usage_calc(self):
        return self._v / 6.5 + 0.5


class Suit(Closes):

    def __init__(self, h):
        self._h = h

    @property
    def material_usage_calc(self):
        return 2 * self._h + 0.3


coat = Coat(52)
suit = Suit(170)
print(coat.material_usage_calc)
print(suit.material_usage_calc)
