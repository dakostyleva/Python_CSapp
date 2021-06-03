
list = ('attribute', 'класс', 'функция', 'type')
new_list = []

for word in list:
    try:
        b_word = bytes(word, 'ASCII')
    except UnicodeEncodeError:
        new_list.append(word)
    continue

print(f'Следующие слова невозможно записать в байтовом типе: {new_list}')