#Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.


def build_list(number):
    result_list = []
    for i in range (1, number + 1):
        element = (1 + 1/i)**i
        result_list.append(round(element, 2))
    return result_list

def find_sum(my_list):
    list_sum = 0
    for elem in my_list:
        list_sum += elem
    print (f"Сумма элементов списка равна: {list_sum}")

n = int(input("Введите количество элементов в последовательности "))
new_list = build_list(n)
print (new_list)
find_sum(new_list)
