#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint

def generate_list(number):
    result_list = []
    for _ in range (number):
        result_list.append(randint(1, 100))
    return result_list


def shuffle_list(input_list):
    result_list = []
    while len(input_list) > 0:
        index = randint(0, len(input_list) - 1)
        result_list.append(input_list[index])
        input_list.pop(index) 
    return result_list

new_list = generate_list(7)
print(new_list)
print(shuffle_list(new_list))

