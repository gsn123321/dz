# number = int(input("grade: "))
# if number <= 50 and number >= 0:
#     print("Незадовільно")
# elif number >= 50 and number <=69:
#     print("Задовільно")
# elif number >= 70 and number <= 89:
#     print("Добре")
# elif number >= 90 and number <= 100:
#     print('Відмінно')
# else:
#     print('помилка')

# money = int(input('зп: '))
# year = int(input("роки: "))
# if year < 1:
#     print("Премія не передбачена")
# elif 1 <= year < 3:
#     bonus = money * 0.05
#     print("премія:", bonus)
# elif 3 <= year < 5:
#     bonus = money * 0.10
#     print("премія:", bonus)
# else:
#     bonus = money * 0.15
#     print("премія:", bonus)

# number = int(input("чотиризначне число: "))
# a = number // 1000
# b = number // 100 % 10
# c = number // 10 % 10
# d = number % 10
# suma = a + b + c + d
# if suma % 2 == 0:
#     print("парні")
# else:
#     print("непарні")

# number = int(input("шестизначне число: "))
# if number < 100000 or number > 999999:
#     print("помилка")
# else:
#     a = number // 100000
#     b = number // 10000 % 10
#     c = number // 1000 % 10
#     d = number // 100 % 10
#     e = number // 10 % 10
#     f = number% 10
#     if a + b + c == d + e + f:
#         print("щасливе число")
#     else:
#         print("нещасливе число")

number = int(input("шестизначне число: "))
a = str(number // 100000)
b = str(number // 10000 % 10)
c = str(number // 1000 % 10)
d = str(number // 100 % 10)
e = str(number // 10 % 10)
f = str(number% 10)
if number < 100000 or number > 999999:
    print("помилка")
else:
    print(f'{f}{e}{c}{d}{c}{a}')





