SRC = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

repeated_nums = set()
unique_nums = set()
for num in SRC:
    if num in unique_nums:
        unique_nums.discard(num)
        repeated_nums.add(num)
    elif num in repeated_nums:
        continue
    else:
        unique_nums.add(num)
unique_nums_ord = [num for num in SRC if num in unique_nums]
print(unique_nums_ord)
