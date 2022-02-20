MAX_NUM = 11

odd_nums_gen = (num for num in range(1, MAX_NUM + 1, 2))
for i in range(7):
    print(next(odd_nums_gen))
