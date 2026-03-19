# try:
#     num1 = float(input('number; '))
#     num2 = float(input('number; '))
#     print(num1 / num2)
# except ValueError:
#     print('wrong number')
# except ZeroDivisionError:
#     print('no zero')
# finally:
#     print('end')


# list = [10, 20, 30, 40, 50]
# try:
#     n = int(input('number: '))
#     print(list[n - 1])
# except ValueError:
#     print('wrong number')
# except IndexError:
#     print('too much')
# finally:
#     print('end')

# try:
#     numbers = input('number: ').split()
#     numbers1 = [int(x) for x in numbers]
#     print(sum(numbers1))
# except ValueError:
#     print('something went wrong')
# finally:
#     print('end')

# try:
#     number = float(input('number: '))
#     if number < 0:
#         raise Exception
#     print(number ** 0.5)
# except Exception:
#     print('no')
# except ValueError:
#     print('no no')
# finally:
#     print('end')


# list = input('через пробыл: ')
# try:
#     tovar, price, number = list.split(', ')
#     price = float(price)
#     number = int(number)
#     print(tovar, price, number)
# except ValueError:
#     print('no')
# finally:
#     print('end')

from random import randint

def func():
    n = randint(1, 2)
    if n == 1:
        return "Підключення успішне"
    elif n == 2:
        raise ConnectionError
try:
    result = func()
    print(result)
except ConnectionError:
    print('Помилка підключення')
finally:
    print('end')

