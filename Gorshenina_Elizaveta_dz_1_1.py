duration = int(input("Введите, пожалуйста, промежуток времени в секундах: "))
print("duration = ", duration)

if duration < 60:
    print(duration, " сек")
elif duration < 60 * 60:
    m = duration // 60
    s = duration % 60
    print(m, " мин ", s, " сек")
elif duration < 60 * 60 * 24:
    h = duration // (60 * 60)
    m = duration % (60 * 60)
    s = m % 60
    m = m // 60
    print(h, " час ", m, " мин ", s, " сек")
else:
    d = duration // (60 * 60 * 24)
    h = duration % (60 * 60 * 24)
    m = h % (60 * 60)
    h = h // (60 * 60)
    s = m % 60
    m = m // 60
    print(d, " дн ", h, " час ", m, " мин ", s, " сек")
