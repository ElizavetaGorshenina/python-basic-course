import os
from shutil import copy2

PROJECT_DIR = './my_project'  # директория папки с проектом

if not os.path.exists(os.path.join(PROJECT_DIR, 'templates')):
    templates_dir = os.path.join(PROJECT_DIR, '_all_templates')
    for root, dirs, files in os.walk(PROJECT_DIR):
        if 'templates' in root.split('\\') and not root.endswith('templates'):
            os.makedirs(os.path.join(templates_dir, root.split('templates\\')[-1]))
            for file in files:
                _all_temp_root = os.path.join(templates_dir, root.split('templates\\')[-1])
                copy2(os.path.join(root, file), _all_temp_root)
    os.rename(templates_dir, os.path.join(PROJECT_DIR, 'templates'))
else:
    print('Папка c шаблонами уже была создана ранее')
