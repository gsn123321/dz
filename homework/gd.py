'''
print("hello, Igor!")
print(10)
print(10 + 10)

day = 5
match day:
    case 1: print("monday")
    case 2: print("s")
    case 3: print("w")
    case 4: print("fe")
    case 5: print("fry")
    case 6: print("frty")
    case 7: print("friday")

if 10 > 5: print("10 > 5")

a = 10
b = 13
print("b") if b > a else print("a")

needed_potatoes = int(input('Картошки: '))
pealed_potatoes = 0

while pealed_potatoes < needed_potatoes:
    print('Беремо картоплю')
    is_rotten = input('Картопля гнила? ')
    if is_rotten == 'так':
        print('Викидаємо')
        continue
    print('Чистимо картоплю...')
    pealed_potatoes += 1
    print(f'Готово! Почищено: {pealed_potatoes}')
    is_tired = input('Ви втомились? ')
    if is_tired == 'так':
        break
else:
    print('Почистили всю картоплю')
print(f'Почистили {pealed_potatoes} картоплі!')


while True:
    num1 = float(input('Введть перше число: '))
    num2 = float(input('Введть дурге число: '))
    action = input("Введіть операцію(+ - * /): ")

    match action :
        case "+":print(f"{num1} + {num2} = {num1 + num2}") 
        case "-":print(f"{num1} - {num2} = {num1 - num2}")
        case "*":print(f"{num1} * {num2} = {num1 * num2}")
        case "/":
            if num2 ==0: print('no')
            else: print(f"{num1} / {num2} = {num1 / num2}")
        case _: print('некоректна операція')
        
    q = input("Input \'q\' to quit or press Enter to cotinue: ")
    if q == "q":
        break
'''

num1 = int(input('Число: '))
num2 = int(input('Число: '))
poradok = input('Порядок(1, 2)? ')

if poradok == '1':
    if num1 > num2:
        while num1 > num2:
            num1 -= 1
            if num1 % 2 > 0:
                print(num1)
            else:
                continue
    else:
        while num2 > num1:
            num2 -= 1
            if num2 % 2 > 0:
                print(num2)
            else:
                continue
elif poradok == '2':
    if num1 < num2:
        while num1 < num2:
            num1 += 1
            if num1 % 2 == 0:
                print(num1)
            else:
                continue
    else:
        while num1 > num2:
            num2 += 1
            if num2 % 2 == 0:
                print(num2)
            else:
                continue