from googletrans import Translator


def num_translate(num):
    _num_var = Translator()
    return _num_var.translate(num, dest='ru', src='en').text


num_for_tr = input('Введите числительное на английском: ')
print('Перевод числительного на русский: ', num_translate(num_for_tr))








