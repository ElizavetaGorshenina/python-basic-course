import sys

sale_num, new_sale = int(sys.argv[1]), float(sys.argv[2].replace(',', '.'))
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    for i in range(sale_num - 1):
        sale = f.readline()
    if not sale:
        print('Записи с таким номером не существует.')
    else:
        position = f.tell()
        f.seek(position)
        f.write('{:010.2f}'.format(
            new_sale).replace('.',
                              ','))  # данный формат предусмотрен для всех записей, что позволяет осуществить корректную перезапись
