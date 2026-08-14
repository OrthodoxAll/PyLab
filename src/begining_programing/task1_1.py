"""
Задачи
Написать функцию, которая получает на вход список чисел и возвращает новый список, содержащий только числа, которые меньше среднего значения списка.
Пример ввода:
[1, 2, 3, 4, 5]

Пример вывода:
[1, 2]
"""


def average(nums):
    # sum = 0
    # len_=len(nums)
    # new_nums=[]
    # for num in nums:
    #     sum += num
    # avg = sum/len_
    # for i in nums:
    #     if i < avg:
    #         new_nums.append(i)
    #
    # return new_nums
    avg = sum(nums) / len(nums)
    return [i for i in nums if i < avg]


nums = [1, 2, 3, 4, 5]
average(nums)
print(average(nums))
