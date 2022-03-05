import re

RE_EMAIL = re.compile(
    r'(^[a-zA-Z0-9](?:[a-zA-Z0-9]|(?:[_\.-](?![_\.@-]))){0,63})@((?:[a-zA-Z0-9](?:[a-zA-Z0-9]|(?:-(?![\.-]))){0,62}\.){1,4}[a-zA-Z]{2,63}$)')
# Регулярное выражение соответствует следующим требованиям к email-адресу:
# - имя пользователя содержит латинские буквы, цифры, символы "_-.",
# не может начинаться и заканчиваться символами "_-.", а также содержать 2
# и более идущих подряд символов "_-.", включает от 1 до 64 символов;
# - доменное имя состоит из 1 домена вержнего уровня и от 1 до 4 поддоменов;
# - домен вержнего уровня содержит от 2 до 63 символов, включающих цифры
# и буквы латинского алфавита;
# - каждый из поддоменов содержит от 1 до 63 символов, включающих цифры,
# буквы латинского алфавита и символ "-", причем не может начинаться и
# заканчиватся символом "-", а также содержать 2 и более идущих подряд
# символа "-".


def email_parse(email_address):
    """Parses email address to username and domain and returns them as a dict"""
    if RE_EMAIL.match(email_address) is None:
        raise ValueError(f'wrong email: {email_address}')
    return {'username': RE_EMAIL.search(email_address).group(1),
            'domain': RE_EMAIL.search(email_address).group(2)}


print(email_parse('Aleksandra_V.V.2022@support.python-lessons.ru'))
