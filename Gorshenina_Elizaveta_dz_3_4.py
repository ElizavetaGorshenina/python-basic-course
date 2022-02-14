def thesaurus_adv(*args):
    names = list(args)
    full_name = names[0].split(' ')
    names_dict = {full_name[1][0]: {full_name[0][0]: []}}
    for name in names:
        full_name = name.split(' ')
        n_letter = full_name[0][0]
        s_letter = full_name[1][0]
        if s_letter in names_dict.keys():
            if n_letter in names_dict[s_letter].keys():
                names_dict[s_letter][n_letter].extend([name])
            else:
                names_dict[s_letter].update({n_letter: name})
        else:
            names_dict.update({s_letter: {n_letter: name}})
    return names_dict


all_names_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(all_names_dict, '\n')
dict_sort = {}
for key_1 in sorted(all_names_dict):
    dict_sort.update({key_1: {}})
    for key_2 in sorted(all_names_dict[key_1]):
        dict_sort[key_1].update({key_2: all_names_dict[key_1][key_2]})
print(dict_sort)

