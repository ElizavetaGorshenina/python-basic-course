from random import choice


def get_jokes(num, flag):
    """
    Returns num jokes created from the given repeating or non-repeating words
    depending on the flag value.
    If num exceeds number of possible jokes with non-repeating words
    returns only possible num jokes and an excuse message.

    :param num: number of requested jokes
    :param flag: indicator of permission for repeats (1 - repeating words,
    0 - non-repeating words)
    :return: list of jokes and a string with an information message
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    def make_choice(words, words_used):
        flag_local = 1
        mes_local = ''
        word = ''
        while flag_local == 1:
            if len(words_used) == len(words):
                mes_local = 'Все неповторяющиеся слова были использованы'
                break
            word = choice(words)
            if word not in words_used:
                words_used.extend([word])
                flag_local = 0
        return word, words_used, mes_local

    jokes = []
    nouns_used = []
    adverbs_used = []
    adjectives_used = []
    mes = ''
    if flag == 0:
        while num:
            noun, nouns_used, mes = make_choice(nouns, nouns_used)
            if len(mes) != 0:
                break
            adverb, adverbs_used, mes = make_choice(adverbs, adverbs_used)
            if len(mes) != 0:
                break
            adjective, adjectives_used, mes = make_choice(adjectives, adjectives_used)
            if len(mes) != 0:
                break
            jokes.extend([noun + ' ' + adverb + ' ' + adjective])
            num -= 1
    else:
        while num:
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)
            jokes.extend([noun + ' ' + adverb + ' ' + adjective])
            num -= 1
    return jokes, mes


jokes_num = input("Сколько различных шуток Вы хотели бы прочесть? ")
flag_general = input("Можно ли повторять слова в шутках? Если да - введите 1, если нет - 0: ")
my_jokes, mes_general = get_jokes(num=int(jokes_num), flag=int(flag_general))
print(*my_jokes, sep='\n')
if len(mes_general) != 0:
    print('\n' + mes_general)
