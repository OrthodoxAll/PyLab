"""Написать функцию, которая получает на вход два списка чисел и возвращает новый список, содержащий только те числа, которые встречаются в обоих списках.

Пример ввода:
[1, 2, 3, 4], [3, 4, 5, 6]

Пример вывода:
[3, 4]"""

from typing import TypeVar

from mypy.meet import typed_dict_mapping_pair

T = TypeVar("T")


def int_list(list1: list[T], list2: list[T]) -> list[T]:
    """Функция получения пересечения списков"""
    # tmp_list=[]
    # for i in list1:
    #     if i in list2:
    #         tmp_list.append(i)
    # return tmp_list
    return [i for i in list1 if i in list2]


# if __name__ == '__task2_1__':
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(int_list(list1, list2))
