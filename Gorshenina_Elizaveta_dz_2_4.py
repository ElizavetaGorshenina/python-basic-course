jobs_and_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']

for el in jobs_and_names:
    name = el.split(' ').pop()
    name = name.upper()
    name = name.title()
    print(f'Привет, {name}!')
