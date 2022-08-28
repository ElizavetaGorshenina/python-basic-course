class MyZeroDivErr(Exception):
    pass


dividend = float(input('Please enter the dividend: '))
try:
    divider = float(input('Please enter the divider: '))
    if divider == 0:
        raise MyZeroDivErr('The divider cannot be equal to zero')
except MyZeroDivErr as err:
    while divider == 0:
        print(err)
        divider = float(input('Please enter the correct divider: '))
finally:
    print('result = ', dividend / divider)
