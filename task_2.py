# Задача 2: Найдите сумму цифр трехзначного числа.

# 1 вариант

NUMBER_LENGTH = 3
number = input('Введите число: ')

if len(number) != NUMBER_LENGTH:
    print(f'Введите {NUMBER_LENGTH}-значное число.')
else:
    result = 0
    for i in range(0, NUMBER_LENGTH):
        result += int(number[i])
    print(f'Сумма цифр числа {number} = {result}')

# 2 вариант

a = int(number) // 100
b = int(number) // 10 % 10
c = int(number) % 10
if len(number) != NUMBER_LENGTH:
    print(f'Введите {NUMBER_LENGTH}-значное число.')
else:
    print(f'Сумма цифр числа {number} = {a + b + c}')
