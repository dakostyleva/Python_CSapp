'''Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''

import json


def write_order_to_jason(item, quantity, price, buyer, date):
    new_values = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json') as file:
        content = json.load(file)
    dict_list = content.get('orders')
    dict_list.append(new_values)
    json_dict = {'orders': dict_list}
    with open('orders.json', 'w') as file:
        json.dump(json_dict, file, indent=4)
    return


write_order_to_jason('cookie', '100', '20000', 'Auchan', '20.01.2019')
write_order_to_jason('milk', '300', '100000', 'Metro', '17.10.2020')
write_order_to_jason('bread', '500', '5000', 'X5', '03.05.2021')
