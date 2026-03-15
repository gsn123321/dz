
# try:
#     value = float(input(': '))
#     unmber = float(input(': '))

#     print(value * (100 - unmber) / 100)
# except ValueError:
#     print('Incorrect number!')



# while True:
#     try:
#         dollar = float(input('dollars: '))
#         kurs = float(input('kurs: '))

#         if kurs == 0:
#             raise Exception
#         print(dollar * kurs)
#     except ValueError:
#         print('Incorrect number!')
#     except Exception:
#         print('Курс обміну не може дорівнювати нулю')
#     finally:
#         konec = input('end? y/n ')
#         if konec.lower == 'y':
#             print('end')
#             break


# try:
#     numbers = input('; ').split()
#     numbers = [int(x) for x in  numbers]
#     print(sum(numbers) / len(numbers))
# except ZeroDivisionError:
#     print('Cant divide by zero!')
# except ValueError:
#     print('Incorrect number!')
# finally:
#     print("Завершення обчислень")

# while True:
#     try:
#         sum = int(input('sum: '))
#         balance = 10000
#         if balance - sum < 0:
#             raise Exception 
#         elif sum % 10 != 0:
#             raise Exception
#         else: print('kruto') 
#     except ValueError:
#         print('Incorrect number!')
#     except Exception:
#         print("Некоректна сума для зняття")
#     finally: 
#         konec = input('end? y/n ')
#         if konec.lower == 'y':
#             print('end')
#             break





# try:
#     code = input(': ')
#     if code[:3] == 'ODR' and code[3:].isdigit():
#         print('vse good ')
#     else:
#         raise Exception
# except Exception:
#     print("Неправильний формат номера замовлення")
# finally:
#     print("Завершення обчислень")


count = 0
total = 0
numbers = input('числa через пробіл: ').split()
try:
    numbers = [x for x in numbers]
    for num in numbers:
        try:
            num = int(num)
            if num != int(num):
                raise ValueError
            else:
                total += num
                count +=1 
        except ValueError:
            print('no number')
    print(total)
    print(total / count)
except ZeroDivisionError:
    print('zero')
finally:
    print('end')















