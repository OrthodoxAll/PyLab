# This is a sample Python script.
# from shlex import split
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from typing import List

import math
from mypy.meet import typed_dict_mapping_pair

#
#
# def int_list(list1:List[int], list2:List[int]) -> List[int]:
#     '''Функция получения пересечения списков'''
#     tmp_list=[]
#     for i in list1:
#         if i in list2:
#             tmp_list.append(i)
#     return tmp_list
#
# if __name__ == '__main__':
#     list1 = [1, 2, 3, 4]
#     list2 = [3, 4, 5, 6]
#
#     print(int_list(list1, list2))
import re





from src.masks import get_mask_card_number, get_mask_account

card_number = input("Введите номер карты: ")
print(get_mask_card_number(card_number))

account_number = input("Введите номер аккаунта: ")
print(get_mask_account(account_number))


def clear_names(file_name: str) -> list:
    """
    Функция для очистки имен от лишних символов
    :param file_name:
    """
    clear_names_list = list()
    try:
        with open("data/" + file_name, encoding="utf-8") as name_file:
            names_list = name_file.read().split()  # Читаем имена из файла
            for name in names_list:
                new_name = ""
                for simbol in name:
                    if simbol.isalpha():
                        new_name += simbol
                if new_name.isalpha():
                    clear_names_list.append(new_name)

        return clear_names_list
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def is_cirillic(name_items: str) -> bool:
    """
    Проверка на введение в строку кириллицы
    """
    return bool(re.search("[а-яА-Я]", name_items))


def filter_russian_names(names_list: str) -> str:
    """
    Фильтрация имен написанных на русском

    :param file_name:
    """
    new_names_list = list()
    for name_item in names_list:
        if is_cirillic(name_item):
            new_names_list.append(name_item)

    return new_names_list


def filter_english_names(names_list: str) -> str:
    """
    Фильтрация имен написанных на английском

    :param file_name:
    """
    new_names_list = list()
    for name_item in names_list:
        if not is_cirillic(name_item):
            new_names_list.append(name_item)

    return new_names_list


def safe_to_file(file_name: str, data: str) -> None:
    """
    Save values in file
    :param file_name:
    :param data:
    """
    with open("data/" + file_name, "w", encoding="utf-8") as names_file:
        names_file.write(data)




if __name__ == "__main__":
    cleared_names = clear_names("names.txt")
    # for i in cleared_names:
    #     print(i)
    filtered_name = filter_russian_names(cleared_names)
    safe_to_file("russian_names.txt", "\n".join(filtered_name))

    filtered_name = filter_english_names(cleared_names)
    safe_to_file("english_names.txt", "\n".join(filtered_name))


def divider(x, y):
    if y >0:
        return x/y
    return 0


def reverse_strring(my_string):
    return my_string[::-1]

def calculate_logarithm(x,base):
    return math.log(x, base)

def calc_avg(my_list):
    if len(my_list) == 0:
        return 0
    return sum(my_list)/len(my_list)

assert calc_avg([1,2,3,4]) == 2.5

assert calc_avg([]) == 0


def finder(my_list, my_type):
    counter = 0
    for item in my_list:
         if isinstance(item, my_type):
             counter += 1
    return counter

