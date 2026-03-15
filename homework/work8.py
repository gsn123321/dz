# my_list = ['aple', 'orange']
# print(my_list[10])

#def recursion():
#    recursion()

#recursion()

#print(10 / 0)


operators = ['+', '-', '*', '/']

while True:
    try:
        num1 = float(input("number: "))
        num2 = float(input('number: '))
        action = input('operation: ')

        if action not in operators:
            raise Exception(action)

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ValueError:
        print('Incorrect number!')    
    except ZeroDivisionError:
        print("Cant divide by zero!")
    except Exception as ex:
        print(f'Incorrect operation! {ex.args[0]}')
    finally: 
        reapeat = input('DO you want to reapeat? y/n ')
        if reapeat.lower() == 'n':
            break