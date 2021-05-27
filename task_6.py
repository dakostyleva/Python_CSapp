
import chardet

with open('text_file.txt', 'rb') as text_file:
    for line in text_file:
        detect = chardet.detect(line)
        print(detect['encoding'])
        line = line.decode(detect['encoding']).encode('utf-8').decode('utf-8')
        print(line)