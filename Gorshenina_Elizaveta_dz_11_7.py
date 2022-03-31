import re


class ComplexNumber:

    RE_C = re.compile(r'^(?P<j_val>[-+]?\d+\.?(\d+)?)j (?P<simple_val>[-+] \d+\.?(\d+)?)$')

    def __init__(self, с_expression):
        self.j_val = float(ComplexNumber.RE_C.match(с_expression).groupdict()['j_val'])
        self.simple_val = float(ComplexNumber.RE_C.match(с_expression).groupdict()['simple_val'].replace(' ', ''))

    def __str__(self):
        if self.simple_val < 0:
            return f'{self.j_val}j - {-self.simple_val}'
        else:
            return f'{self.j_val}j + {self.simple_val}'

    def __add__(self, other):
        sum_j_val = self.j_val + other.j_val
        sum_simple_val = self.simple_val + other.simple_val
        if sum_simple_val < 0:
            return ComplexNumber(f'{sum_j_val}j - {-sum_simple_val}')
        else:
            return ComplexNumber(f'{sum_j_val}j + {sum_simple_val}')

    def __mul__(self, other):
        mul_j_val = self.j_val * other.simple_val + self.simple_val * other.j_val
        mul_simple_val = - (self.j_val * other.j_val) + self.simple_val * other.simple_val
        if mul_simple_val < 0:
            return ComplexNumber(f'{mul_j_val}j - {-mul_simple_val}')
        else:
            return ComplexNumber(f'{mul_j_val}j + {mul_simple_val}')


c_num_1 = ComplexNumber('-1.4j + 0.18')
c_num_2 = ComplexNumber('8j - 3.911')
print(c_num_1.j_val)
print(c_num_1.simple_val)
print(c_num_1 + c_num_2)
print(c_num_1 * c_num_2)
