# Задача № 5
# Реализуйте алгоритм перемешивания списка.
import random 

n = int(input('Введите кол-во элементов списка: '))
a = [input(f'Введите элмент № {i+1}: ') for i in range(n)]
print('Исходный список', a)
random.shuffle(a)
print('Перемешанный список', a)