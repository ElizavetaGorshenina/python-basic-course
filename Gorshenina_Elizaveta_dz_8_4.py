from functools import wraps


def val_checker(check_func):
    def type_logger(callback):
        @wraps(callback)
        def wrapper(*args):
            for arg in args:
                if not check_func(arg):
                    raise ValueError(f'wrong val {arg}')
            callback_result = callback(*args)
            print(callback_result, type(callback_result), sep=', ')
            return ', '.join(
                [f'{callback.__name__}({key}: {type(key)}, {val}: {type(val)})' for key, val in
                 callback_result.items()])

        return wrapper

    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(*nums):
    """Calculates cubes of numbers"""
    return {num: num ** 3 for num in nums}


print(calc_cube(3, 6.6, 45))
help(calc_cube)
print(calc_cube(-5))
