'''Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с
юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''

import yaml

items_list = ['milk', 'cookie', 'chocolate', 'bread', 'juice']
items_quantity = len(items_list)
items_price = {'milk': '50₽', 'cookie': '30₽', 'chocolate': '70₽', 'bread': '40₽', 'juice': '55₽'}

data_to_yaml = {'items_list': items_list, 'items_quantity': items_quantity, 'items_price': items_price}

with open('new_file.yaml', 'w') as file:
    yaml.dump(data_to_yaml, file, default_flow_style=False, allow_unicode=True)
with open('new_file.yaml') as file:
    print(file.read())
