prices = [59.99, 408.19, 108, 55.09, 39.9, 165, 580.7, 114.08, 126.5, 205.1, 1200]
price_list = ''
for price in prices:
    rubs = str(int(price * 100 // 100))
    kopecks = int(price * 100 % 100)
    if kopecks < 10:
        kopecks = str(kopecks)
        kopecks = '0' + kopecks
    kopecks = str(kopecks)
    price_list += f'{rubs} руб {kopecks} коп, '
print(price_list)

print(prices)
print("Идентификатор списка:", id(prices))
prices.sort()
print(prices)
print("Идентификатор отсортированного списка:", id(prices))
prices_sorted = sorted(prices, reverse=True)
print(prices_sorted)
print("Идентификатор нового отсортированного списка:", id(prices_sorted))
print(prices_sorted[4::-1])
