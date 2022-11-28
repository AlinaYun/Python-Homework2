# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

from random import randint

# - создает список из рандомных четырех значных чисел
def create_list (number_of_elem):
    result_list = []
    for _ in range (number_of_elem):
        result_list.append(randint(1000, 10000))
    return result_list

# - принимает с консоли цифру и удаляет ее из всех элементов списка
def delete_digit(list, number_to_delete):
    for i in range(len(list)):
        list[i] = str(list[i])
        if number_to_delete in list[i]:
            list[i] = list[i].replace(number_to_delete, '')
        list[i] = int(list[i])
    return list

# - цифры каждого элемента суммирует пока результат не станет однозначным числом
def replace_element(list):
    for i in range(len(list)):
        while list[i] > 9:
            list[i] = sum_digits(list[i])
    return list 

def sum_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number//10)

# - из финального списка убирает все дублирующиеся элементы

def delete_duplecates(list):
    new_list = []
    for elem in list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

number_to_delete = input("Введите число: ")
my_list = delete_digit([2634, 6934, 7286, 3353, 4602, 3176, 3796], number_to_delete)
print(my_list)
my_list = replace_element(my_list)
print(my_list)
my_list = delete_duplecates(my_list)
print(my_list)