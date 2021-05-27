
list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in list:
    enc_word = word.encode('utf-8')
    print(enc_word)
    dec_word = enc_word.decode('utf-8')
    print(dec_word)
