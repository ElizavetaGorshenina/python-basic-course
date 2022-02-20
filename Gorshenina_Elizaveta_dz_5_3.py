TUTORS = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
KLASSES = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_tuples(first_list, second_list):
    for ind in range(len(first_list)):
        if ind >= len(second_list):
            pair = first_list[ind], None
        else:
            pair = first_list[ind], second_list[ind]
        yield pair


tutorship = gen_tuples(TUTORS, KLASSES)
for i in range(len(TUTORS)):
    print(next(tutorship))
check_var = tutorship
print(next(check_var))
