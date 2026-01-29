# num1 = int(input('Число: '))
# num2 = int(input('Число: '))

# if num1 > num2:
#     num1, num2 = num2, num1
# print("Усі числа:")
# i = num1
# while i <= num2:
#     print(i, end=" ")
#     i += 1
# print("У спадному порядку:")
# i = num2
# while i >= num1:
#     print(i, end=" ")
#     i -= 1
# print("Кратні 7:")
# i = num1
# while i <= num2:
#     if i % 7 == 0:
#         print(i, end=" ")
#     i += 1
# count = 0
# i = num1
# while i <= num2:
#     if i % 5 == 0:
#         count += 1
#     i += 1
# print("Кількість кратних 5:", count)

# num1 = int(input("Число: "))
# num2 = int(input("Число: "))

# if num1 > num2:
#     num1, num2 =num2, num1

# i = num1 
# while i <= num2:
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1

# num1 = int(input("Початок: "))
# num2 = int(input("Кінець: "))
# step = int(input("Крок: "))
# order = input("1, 2: ")

# if step <= 0:
#     print("ні")
# else:
#     if num1 > num2:
#         num1, num2 = num2, num1

#     if order == "1":
#         i = num1
#         while i <= num2:
#             print(i, end=" ")
#             i += step
#     else:
#         i = num2
#         while i >= num1:
#             print(i, end=" ")
#             i -= step

# num2 = int(input("Початок: "))
# num1 = int(input("Кінець: "))
# if num2 > num1:
#     num2, num1 = num1, num2

# i = num2
# product = 1

# while i <= num1:
#     if i % 4 == 0 and i % 6 != 0:
#         product *= i
#     i += 1

# if product != 1:
#     print("Добуток:", product)
# else:
#     print("Ні")

A = int(input("A: "))
N = int(input("N: "))
result = 1
i = 1
while i <= N:
    result = result * A
    i += 1
print("Результат:", result)