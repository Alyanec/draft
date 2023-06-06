# Зад_1
def calculate_sum(lst):
    total_sum = 0
    index = 0
    length = len(lst)

    while index < length:
        total_sum += lst[index]
        index += 1

    return total_sum

my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print("Сумма элементов списка:", result)

# Зад_2
a = 1.2
n = 2

while True:
    number = 1 + 1 / n

    if number < a:
        break

    print(number)

    n += 1

# Зад_4
def count_occurrences(string_list, character):
    occurrences = []
    for string in string_list:
        count = string.count(character)
        occurrences.append(count)
    return occurrences

strings = ["apple", "banana", "cherry"]
character = "a"
result = count_occurrences(strings, character)
print(result)

# Зад_5
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
number = int(input("Введите число: "))
if number in list_:
    print("Число", number, "найдено в списке.")
else:
    print("Число", number, "не найдено в списке.")

def some_function(a):
    b = 2
    c = 3
    return a, b, c
a = 1
function_a, _, function_c, = some_function(a)
print(function_a)
print(function_c)





