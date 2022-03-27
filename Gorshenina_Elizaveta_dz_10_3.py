class Cell:

    def __init__(self, cells_num):
        self.cells_num = cells_num

    def __str__(self):
        return f'{self.cells_num}'

    def __add__(self, other):
        return Cell(self.cells_num + other.cells_num)

    def __sub__(self, other):
        if self.cells_num > other.cells_num:
            return Cell(self.cells_num - other.cells_num)
        else:
            return 'Operation is not available'

    def __mul__(self, other):
        return Cell(self.cells_num * other.cells_num)

    def __floordiv__(self, other):
        return Cell(self.cells_num // other.cells_num)

    def make_order(self, row_size):
        return ("*" * row_size + "\\n") * (self.cells_num // row_size) + "*" * (self.cells_num % row_size)


cell_1 = Cell(12)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
