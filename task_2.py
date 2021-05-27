list = ('class', 'function', 'method')

for word in list:
    word_bytes = bytes(word, 'utf-8')
    print(word_bytes)
    print(type(word_bytes))
    print(f'длина равна {len(word_bytes)}')