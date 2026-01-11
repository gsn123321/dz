
# number = int(input('число: '))
# if number % 2 == 0:
#     print('четное')
# else:
#     print('не')

# number = int(input('число: '))
# if number % 7 == 0:
#     print('кратне 7')
# else:
#     print('не')

# number1 = int(input('перше: '))
# number2 = int(input('друге: '))

# if number1 - number2 < 0:
#     print('перше число меньше')
#     print(number1)
# else:
#     print('друге число меньше')
#     print(number2)


# number1 = int(input('Введіть число:'))
# number2 = int(input('Введіть число:'))

# operation = input('Оберіть операцію (+ - * середнє): ')

# if operation == '+':
#     print(f'{number1} + {number2} = {number1 + number2}')
# elif operation == '-':
#     print(f'{number1} - {number2} = {number1 - number2}')
# elif operation == '*':
#     print(f'{number1} * {number2} = {number1 * number2}')
# elif operation == 'середнє':
#     print(f'({number1} + {number2}) / 2 = {(number1 + number2) / 2}')
# else:
#     print('Некоректна операція')


sum = float(input('сума: '))
v = input('валюта: ')
kurs = float(input('курс: '))
if v == "євро":
    print(f'{sum / kurs}')
elif v == 'гривні':
    print(f'{sum / kurs}')
elif v == 'фунти':
    print(f'{sum / kurs}')
else:
    print('Error')


























