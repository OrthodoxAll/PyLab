# This is a sample Python script.
# from shlex import split
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

def clear_names(file_name: str) -> list:
    """
    Функция для очистки имен от лишних символов
    :param file_name:
    """
    clear_names_list= list()
    try:
        with open("data/" + file_name, encoding='utf-8') as name_file:
            names_list = name_file.read().split()  # Читаем имена из файла
            for name in names_list:
                new_name = ''
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

if __name__ == '__main__':
    cleared_names = clear_names('names.txt')
    for i in cleared_names:
        print(i)
