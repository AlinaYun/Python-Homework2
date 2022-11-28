# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def find_sum(number):
    sum_of_digits = 0
    for digit in number:
        if digit.isdigit():
            sum_of_digits += int(digit)
    print(sum_of_digits)

given_number = input("Введите число: ")
find_sum(given_number)