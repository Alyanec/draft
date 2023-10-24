#                                              Задання_1
# a = int(input("Введіть число a: "))
# b = int(input("Введіть число b: "))
#
# c = [x**2 for x in range(a + 1, b)]
# print("Квадрат між числами", a, "и", b, ":", c)
#                                              Завдання_2
# numbers = []
# while True:
#     user_input = input("Введіть число ілі 'end' для завершення: ")
#     if user_input == 'end':
#         break
#     try:
#         number = int(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Невірний ввід. Будь ласка, введіть число ілі 'end'.")
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print("Непарні числа в спискі:", odd_numbers)
#                                              Завдання_3
# numbers = []
# even_count = 0
# odd_count = 0
#
# while True:
#     user_input = input("Введіть число ілі 'end' для завершення: ")
#
#     if user_input == 'end':
#         break
#
#     try:
#         number = int(user_input)
#
#         numbers.append(number)
#
#         if number % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     except ValueError:
#         print("Некоректне введення. Введіть число або 'end'.")
#
# print("Список введених чисел:", numbers)
# print("Кількість парних чисел:", even_count)
# print("Кількість непарних чисел:", odd_count)
#                                           Завдання_4
# numbers = [1, 3, 5, 2, 7, 6]
#
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         print(numbers[i])
#                                           Завдання_5
# def swap_min_max(numbers):
#     if not numbers:
#         return numbers
#
#     min_index = numbers.index(min(numbers))
#     max_index = numbers.index(max(numbers))
#
#     numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
#
#     return numbers
#
# numbers = [3, 9, 1, 6, 5, 2]
# swapped_numbers = swap_min_max(numbers)
# print(swapped_numbers)
#                                             Завдання_6
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements = len(set(my_list))
# print("Кількість різних елементів:", unique_elements)
#                                              Завдання_8
# def cyclic_shift_right(lst):
#     if len(lst) <= 1:
#         return lst
#
#     last_element = lst[-1]
#
#     for i in range(len(lst) - 1, 0, -1):
#         lst[i] = lst[i - 1]
#
#     lst[0] = last_element
#
#
# my_list = [1, 2, 3, 4, 5]
# cyclic_shift_right(my_list)
# print(my_list)
#                                             Завдання_10
# import random
#
# n = int(input("Введіть кількість елементів: "))
# min_value = int(input("Введіть мінімальне значення: "))
# max_value = int(input("Введіть максимальне значення: "))
#
# if min_value > max_value:
#     print("Мінімальне значення не може бути більшим за максимальне.")
# else:
#     random_numbers = [random.randint(min_value, max_value) for _ in range(n)]
#
#     print("Згенерований список:", random_numbers)