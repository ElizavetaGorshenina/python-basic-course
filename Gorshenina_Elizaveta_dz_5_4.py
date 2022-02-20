SRC = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

greater_nums = [SRC[ind + 1] for ind in range(len(SRC) - 1) if SRC[ind + 1] > SRC[ind]]
print(greater_nums)
