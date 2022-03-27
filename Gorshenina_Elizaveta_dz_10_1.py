import copy


class Matrix:

    def __init__(self, list_of_lists):
        self.num_rows = len(list_of_lists)
        self.num_columns = len(list_of_lists[0])
        self.els = list_of_lists

    def __str__(self):
        self.els_str = ''
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                self.els_str += f'\t{str(self.els[i][j])}'
            self.els_str += '\n'
        return self.els_str

    def __add__(self, other):
        matrix_sum = copy.copy(self.els)
        if self.num_rows != other.num_rows or self.num_columns != other.num_columns:
            return 'The matrices are of different dimension \n'
        else:
            for i in range(self.num_rows):
                for j in range(self.num_columns):
                    matrix_sum[i][j] += other.els[i][j]
            return Matrix(matrix_sum)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_4 = Matrix([[4, 3], [3, 7], [4, 9]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_4)
print(matrix_3 + matrix_4)
print(matrix_1 + matrix_4)
