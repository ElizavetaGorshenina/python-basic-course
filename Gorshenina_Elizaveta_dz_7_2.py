import os

TARGET_DIR = './'  # директория для размещения папки с проектом

with open('config.yaml', 'r', encoding='utf-8') as f_config:
    while True:
        link = f_config.readline().strip()
        if not link:
            break
        f_path = os.path.join(TARGET_DIR, link)
        if not os.path.exists(f_path):
            if f_path.endswith('.py') or f_path.endswith('.html'):
                _ = open(f_path, 'x')
                _.close()
            else:
                os.mkdir(f_path)
        else:
            print(f'Папка/файл "{f_path}" уже был/а создан/а ранее')
