for i in range(100):
    i += 1
    if i % 100 == 11 or i % 100 == 12 or i % 100 == 13 or i % 100 == 14:
        ending = "процентов"
    elif i % 10 == 1:
        ending = "процент"
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        ending = "процента"
    else:
        ending = "процентов"
    print(i, " ", ending)

