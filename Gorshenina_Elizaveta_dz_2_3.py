elements = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(elements))

idx = 0
while idx < len(elements):
    if elements[idx].isdigit():
        if len(elements[idx]) < 2:
            elements[idx] = "0" + elements[idx]
        elements.insert(idx, '"')
        elements.insert(idx + 2, '"')
        idx += 2
    elif (elements[idx].startswith('+') or elements[idx].startswith('-')) and elements[idx][1:].isdigit():
        if len(elements[idx][1:]) < 2:
            elements[idx] = elements[idx][0] + "0" + elements[idx][1:]
        elements.insert(idx, '"')
        elements.insert(idx + 2, '"')
        idx += 2
    idx += 1
print(elements)
print(id(elements))

phrase = ""
quotes_counter = 0
for el in elements:
    if el != '"':
        if quotes_counter % 2 == 0:
            phrase = phrase + el + ' '
        else:
            phrase = phrase + el
    else:
        quotes_counter += 1
        if quotes_counter % 2 != 0:
            phrase = phrase + el
        else:
            phrase = phrase + el + ' '

if phrase[-1] == ' ':
    phrase = phrase[:-1]
print(phrase)

