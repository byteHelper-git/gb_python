# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def my_func(n1, n2):
    return n1 + n2


even_numbers = [x for x in range(100, 1001, 2)]

print(reduce(my_func, even_numbers))
