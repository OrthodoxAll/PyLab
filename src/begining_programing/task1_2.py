# Написать функцию, которая получает на вход список строк и возвращает новый список, содержащий только уникальные строки.
# Пример ввода:
# ['apple', 'banana', 'orange', 'apple']
#
# Пример вывода:
# ['apple', 'banana', 'orange']


def set_list(my_list):
    # set_= set(list)
    # return set_
    return list(set(my_list))


my_list = ["apple", "banana", "orange", "apple"]

set_ = set_list(my_list)
print(set_)
print(type(set_))
