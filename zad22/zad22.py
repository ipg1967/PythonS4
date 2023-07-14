# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint


def make_array(n):
    a = 1
    b = 10
    array = [randint(a, b) for i in range(n)]
    print(f"создан массив чисел - {array}")
    return array


n = int(input("Введите число элементов первого массива: "))
numbers_1 = set(make_array(n))
n = int(input("Введите число элементов второго массива: "))
numbers_2 = set(make_array(n))
# print(numbers_1)
# print(numbers_2)
list = numbers_1.intersection(numbers_2)
print(f"Пересечение списков: {list}")
