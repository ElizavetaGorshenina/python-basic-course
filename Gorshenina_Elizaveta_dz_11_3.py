import re


class MyTypeErr(Exception):
    pass


RE_NUM = re.compile(r'^[-+]?\d+\.?(\d+)?$')
the_list = []
while True:
    try:
        el = input('Please enter an element or "stop" to complete the list: ')
        if el == 'stop' or el == 'Stop':
            break
        elif RE_NUM.match(el):
            the_list.append(float(el))
        else:
            raise MyTypeErr('The element is of a wrong type. It is not added to the list')
    except MyTypeErr as err:
        print(err)
print(the_list)
