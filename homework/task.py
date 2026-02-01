# num1 = int(input('Чтсло: '))

# for i in range(1, 11):
#     print(f'{num1} * {i} = {num1 * i} ')



# for i in range(1, 11):
#     for j in range(1,10):
#         print(f'{j} * {i} = {j * i} ')
#     print()

# g = int(input('Скільки чисел: '))
# d = int(input("Яке число: "))
# for i in range(1, g):
#     f = int(input("Яке число: "))
#     if f > d:
#         d = f
# print(f'число{d}')

# import random
# random_number = random.randint(1, 501)
# a = 0
# while True:
#     number = int(input("Число: "))
#     if number == 0:
#         break 
#     a += 1
#     if number < random_number:
#         print("меньше")
#     elif number > random_number:
#         print("Більш9е")
#     else:
#         print(f"Наконецто, {a} спроб")
#         break

type1 = input("Квадрат чи прямокутник: ")
s = input("Символ: ")
if type1 == 'квадрат':
    w = int(input("см: "))
    for i in range(w):
        print(s * w)
elif type1 == 'прямокутник':
    w1 = int(input("см: "))
    d = int(input("см: "))
    for i in range(w1):
        print(s * d)