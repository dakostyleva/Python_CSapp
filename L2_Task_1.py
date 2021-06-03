'''Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений
извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка —
например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать
главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных
данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''

import csv
import re


def param_extraction(param, text):
    search_result = re.findall(param, text)
    result_split = re.split(r': +', search_result[0])
    param_value = result_split[1]
    return param_value


def get_data():
    data_list = [param_name_list]
    for file in files_list:
        with open(file, 'r', encoding='windows-1251', errors='ignore') as new_file:
            content = new_file.read()
        param_list = []
        for i in re_param_name_list:
            y = param_extraction(i, content)
            param_list.append(y)
        data_list.append(param_list)
    return data_list


files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
param_name_list = ['Название ОС', 'Версия ОС', 'Изготовитель ОС', 'Тип системы']
re_param_name_list = {r'{}[^\n]*'.format(re.escape(x)) for x in param_name_list}

main_data = get_data()
print(main_data)


def write_to_csv(csv_file):
    with open(csv_file, 'w') as file_2:
        file_2_writer = csv.writer(file_2)
        for row in main_data:
            file_2_writer.writerow(row)
    with open(csv_file) as file_3:
        print(file_3.read())


write_to_csv('csv_report.csv')
