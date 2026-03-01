# def print_contact(contact):
#     if contact['мобільний'] != None: print(f'мобільний: {contact[name]['мобільний']}')
#     if contact['робочий'] != None: print(f'робочий: {contact[name]['робочий']}')

# contacts = {
#     'Настя' : {
#         'мобільний': '0506985764',
#         'робочий' : '0890989584'
#     },
#     'Антон СТО' : {
#         'мобільний': None,
#         'робочий' : '0500598473'
#     },
#     'Тимофій Карпати' : {
#         'мобільний': '0506985764',
#         'робочий' : None
#     }
# }
# print('1. Знайти контакт\n2. Вивести всі контакти\n0. Вихід')

# action = int(input('Оберіть дую:'))

# while True:
#     match action:
#         case 1:
#             name = input('імя контакту: ')
#             if name in contacts:
#                 print_contact(contacts[name])
#             else:
#                 print("no")
#         case 2:
#             for contact in contacts:
#                 print(contact)
#                 print_contact(contacts[name])
#         case 0: break
#         case _: print('no')

# def print_greeeting():
#     print('==================')
#     print('== hello, user! ==')
#     print('==================')


# print_greeeting()

# def print_named_greeting(name: str = "guest") -> None:
#     print('==================')
#     print(f'== hello, {name.upper()}! ==')
#     print('==================')

# print_named_greeting('Vova')
# print_named_greeting()
# # print_named_greeting(10)

# def sum(num1: float | int, num2: float | int) -> float | None:
#     if type(num1) != float or type(num2) != float:
#         return
#     return num1 + num2
# result = sum(10.0,12.0)
# print(result)

# def print_full_name(last_name, first_name):
#     print('Повне імя:', last_name, first_name)

# print_full_name('Ковальчук', 'Антон')
# print_full_name(last_name='Ковальчук', first_name='Антон')

# def my_animal(type, name, age):
#     print(f'У мене є {type} на імя {name}. Вік: {age}')

# my_animal('Собака', age=10, name='Патрон')    

# def only_positional(param, /):
#     print(param)

# # only_positional(param=10)

# def only_key_word(*, param):
#     print(param)

# only_key_word(10)

# print(10, 20 ,30 ,40)
# print(1, 2, 3,4 ,5, 5, 6, 6)

# def my_sum(*numbers):
#     result = 0
#     for i in numbers:
#         result += i
#     return result
# print(my_sum(10,10))

# def my_func(**kwargs):
#     for i in kwargs:
#         print(i, kwargs[i], sep=': ')
# my_func(name="Vova", age = 22, pet='cat')

# def unpack_positional(a,b,c):
#     print(a,b,c, sep=': ')
# fruits = ['apple', 'orange', 'banana']
# unpack_positional(*fruits)

# def unpack_kw_args(red,green,yellow):
#     print(red, green, yellow)

# fruits= {
#     'red': 'apple',
#     'green': 'pear',
#     'yellow': 'banana'
# }
# unpack_kw_args(**fruits)


# def enclosing_func():
#     enclosing_var = 10
#     def inner_func():
#         print(enclosing_var)
#     inner_func()
# enclosing_func()

def do_smth():
    print('smth')

def main():
    print('start')    
    do_smth()
    print('end')

if __name__ == '__main__':
    main()




    
# global_var = 12

# def local_func(local_param):
#     global global_var
#     global_var = 40
#     local_var=10
#     print(local_var)
#     print(global_var)

# local_func(10)
# print(global_var)
# print(local_var)
# print(local_param)
















