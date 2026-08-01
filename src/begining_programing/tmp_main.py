"""
from utils.add import *



print(add(1,2))

import os

current_directory = os.getcwd()
print(current_directory)

directory_files = os.listdir(current_directory)
print(directory_files)

def task():
    print('hello world')


if __name__ == '__main__':
    task()

with open('log.txt','w', encoding='utf-8') as f:
    f.write('Log Entry 1\n')

with open('log.txt','r', encoding='utf-8') as f:
    contend = f.read()
    print('Содержимое файлва после первой записи')
    print(contend)

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Log Entry 2\n')

with open('log.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Содержимое файла после добавления нового лог-сообщения:")
    print(content)

with open('shopping_list.txt', 'w', encoding='utf-8') as f:
    f.write('Milk\n')
    f.write('Bread\n')
    f.write('Eggs\n')
"""

# with open('exemple.txt', 'r', encoding='utf-8') as f:
# print(f.read())


# with open('shopping_list.txt', 'a', encoding='utf-8') as f:
# f.write('Бутер\n')
#  f.write('Хлеб\n')
import os

base_path = os.path.dirname(__file__)
print(base_path)
# base_path = 'E:\\Digital\\bakend_programm\\my_prj'
full_path = os.path.join(base_path, "data", "exemple.txt")
with open(full_path, "r", encoding="utf-8") as f:
    print(f.read())
