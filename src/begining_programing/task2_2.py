"""
2 Написать функцию, которая получает на вход список чисел и возвращает новый список, содержащий только числа, которые являются палиндромами.
Пример ввода:
[121, 123, 131, 34543]

Пример вывода:
[121, 131, 34543]
"""

from typing import List


def get_polindroms(nums_list: List[int]) -> List[int]:
    """Возвращает список чисел"""
    # polindroms = []
    # for num in nums_list:
    #     if str(num) == str(num)[::-1]:
    #         polindroms.append(num)
    # return polindroms
    return [num for num in nums_list if str(num) == str(num)[::-1]]


if __name__ == "__main__":
    print(get_polindroms([121, 123, 131, 34543]))
