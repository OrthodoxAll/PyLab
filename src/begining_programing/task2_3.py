'''Написать функцию, которая получает на вход два списка чисел и возвращает новый список, содержащий только те числа, которые есть только в одном из списков.
Пример ввода:
[1, 2, 3, 4], [3, 4, 5, 6]

Пример вывода:
[1, 2, 5, 6]'''


def get_inter(nums_list_1:list[int], nums_list_2:list[int]) -> list[int]:
    # list_inter = (set(nums_list_1)-set(nums_list_2)).union(set(nums_list_2)- set(nums_list_1))
    return list(set(nums_list_1).symmetric_difference(set(nums_list_2)))

print(get_inter([1, 2, 3, 4], [3, 4, 5, 6]))
