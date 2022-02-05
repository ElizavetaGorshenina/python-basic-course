i = 0
cubes = []

while True:
    i += 1
    if i >= 1000:
        break
    elif i % 2 != 0:
        cubes.append(i * i * i)

print(cubes)

sum_of_cubes = 0

for cube in cubes:
    int_part = cube // 10
    rem_part = cube % 10
    sum_of_nums = 0
    while True:
        sum_of_nums += rem_part
        if int_part == 0:
            break
        rem_part = int_part % 10
        int_part = int_part // 10

    if sum_of_nums % 7 == 0:
        sum_of_cubes += cube

print("Сумма чисел из списка, сумма цифр которых делится нацело на 7: ", sum_of_cubes)
