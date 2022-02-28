import os
import json

TARGET_DIR = './'


def pstv_num_exp(num):
    if num > 0:
        counter = 0
        while num // 10 != 0:
            counter += 1
            num = num // 10
    return counter


stat_dict = {}
for root, dirs, files in os.walk(TARGET_DIR):
    for item in os.scandir(root):
        if os.path.isfile(item):
            size_range = os.stat(item).st_size
            if size_range != 0:
                size_range = 10 ** pstv_num_exp(size_range)
            ext = os.path.splitext(item.name)[-1]
            if size_range in stat_dict.keys():
                stat_dict[size_range][0] += 1
                if ext not in stat_dict[size_range][1]:
                    stat_dict[size_range][1].extend([ext])
            else:
                stat_dict.update({size_range: [1, [ext]]})
stat_dict_sort = {}
for key in sorted(stat_dict):
    stat_dict_sort[key] = tuple(stat_dict[key])
stat_dict_sort_str = json.dumps(stat_dict_sort)
with open(os.path.basename(os.path.abspath(TARGET_DIR)) + '_summary.json', 'w', encoding='utf-8') as f:
    f.write(stat_dict_sort_str)
