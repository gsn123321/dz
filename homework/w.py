'''
print("Hello, world")
print(10)
print(10, 12, 14)
print(10, 5, 6, 6 ,sep=', ')

# Тип даних - характеристика даних, яка визначає діапазон значень та набір доступних операцій.

# str - послідовність символів
# int - цілі числа
# float - дробові числа

print(type(10 / 5))

# Змінна - іменована область пам'яті, що зберігає значення певного типу і може його змінювати
# протягом виконання програми.

group = 'П511'
print(type(group))
group = 511
print(type(group))

weather = input('Введіть поточну погоду: ')
print(weather)


number1 = float(input("Введіть число: "))
print(type(number1))
number2 = float(input("Введіть число: "))
print(f'{number1} ** {number2} = {number1 ** number2}')


# bool - True або False

can_pinguins_swim = True
can_pinguins_fly = False

print(f'Чи можуть пінгвіни плавати? {can_pinguins_swim}')
print(f'Чи можуть пінгвіни літати? {can_pinguins_fly}')
print(type(can_pinguins_fly))
print(type(can_pinguins_swim))


number = int(input('число: '))
print(f'{number} > 10? {number > 10}')
print(f'{number} <= 10? {number <= 10}')
print(f'{number} < 10? {number < 10}')
print(f'{number} >= 10? {number >= 10}')
print(f'{number} != 10? {number != 10}')
print(f'{number} == 10? {number == 10}')


is_raining = input('Чи йде дощ? ')
if is_raining == 'так':
    print('парасолю бери')

# is_cold = input('зараз холодно? ')
# if is_cold == 'так':
#     print('вдягни теплий одяг')
# else:
#     print('вдягни легкий одяг')

temp = int(input('Скільки зараз градусів на вулиці? '))
if temp <= -10:
    print('Вдягнись дуже тепло')
elif temp > -10 and temp <= 5:
    print('вдягнись тепло')
elif temp > 5 and temp <= 16:
    print('Вдягни кофту')
else:
    print('Як хоч')





print('виходимо')

# оператори об'єднання - and и or - об'єднують результати двох логічних виразів


# not - інвертує значення bool
print(f'not True = {not True}')
print(f'not False = {not False}')


# number = int('10')

boolean = bool(0) #FAlse
print(bool(0)) #false
print(bool(0.0)) #False
print(bool('')) # false

something = None
print(bool(something))
print(bool(10)) # True
print(bool(-6.8)) # True
print(bool('hello')) # True


number1 = int(input('Введіть число:'))
number2 = int(input('Введіть число:'))

operation = input('Оберіть операцію (+ - * /): ')

if operation == '+':
    print(f'{number1} + {number2} = {number1 + number2}')
elif operation == '-':
    print(f'{number1} - {number2} = {number1 - number2}')
elif operation == '*':
    print(f'{number1} * {number2} = {number1 * number2}')
elif operation == '/':
    if number2 == 0:
        print('Не можна ділити на нуль')
    print(f'{number1} / {number2} = {number1 / number2}')
else:
    print('Некоректна операція')
'''
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


























