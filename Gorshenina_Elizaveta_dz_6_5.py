import sys
import os

link_1 = input('Введите путь к 1 исходному файлу: ')
link_2 = input('Введите путь ко 2 исходному файлу: ')
link_3 = input('Введите путь к файлу с результатом работы программы: ')
with open(link_1, 'w', encoding='utf-8') as f_users:
    f_users.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович\nПетров,Илья,Петрович')
with open(link_2, 'w', encoding='utf-8') as f_hobby:
    f_hobby.write('скалолазание,охота\nгорные лыжи')
with open(link_1, 'r', encoding='utf-8') as f_users:
    with open(link_2, 'r', encoding='utf-8') as f_hobby:
        with open(link_3, 'a', encoding='utf-8') as f_users_hobby:
            while True:
                user = f_users.readline().strip()
                hobby = f_hobby.readline().strip()
                if (not user) & bool(hobby):
                    os.system('echo "Программа прекратила работу. Exit code 1"')
                    sys.exit(1)
                if bool(user) & (not hobby):
                    hobby = None
                if not user:
                    break
                f_users_hobby.write(f'{user}: {hobby}\n')
