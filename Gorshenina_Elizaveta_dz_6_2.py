with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    info_dict = {}
    while True:
        row = f.readline()
        if not row:
            break
        remote_addr = row.split(' - - ')[0]
        if remote_addr in info_dict.keys():
            info_dict[remote_addr] += 1
        else:
            info_dict.update({remote_addr: 1})
max_val = 0
for key, val in info_dict.items():
    if val > max_val:
        max_val = val
        spamer_addr = key
print(f'Спамером является "{spamer_addr}", отправивший {max_val} запросов.')
