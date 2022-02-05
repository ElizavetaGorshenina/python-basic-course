i = 0
cubes = []

while True:
    i += 1
    if i >= 1000:
        break
    elif i % 2 != 0:
        cubes.append(i * i * i)

sum_of_values = 0

for cube in cubes:
    temp_var = cube + 17
    int_part = temp_var // 10
    rem_part = temp_var % 10
    sum_of_nums = 0
    while True:
        sum_of_nums += rem_part
        if int_part == 0:
            break
        rem_part = int_part % 10
        int_part = int_part // 10

    if sum_of_nums % 7 == 0:
        sum_of_values += temp_var

print("Сумма чисел, сумма цифр которых делится нацело на 7: ", sum_of_values)
