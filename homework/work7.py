# employees = {
#     '1': {
#         'name' : 'Антон',
#         'position': 'Junior .NET Developer',
#         'salary': 20000
#     },
#     '2': {
#         'name' : 'Анастасія',
#         'position':'Team Lead',
#         'salary': 115000
#     },
#     '3': {
#         'name' : 'Кирило',
#         'position': 'Senior .NET Developer',
#         'salary': 90000
#     }
# }

# print(employees['2']['position'])













# new_dictionary = dict()
# new_dictionary = {
#     "key": "value",
#     10: 15.8

# }

contacts = {
    'Антон': '0506959068',
    'Ліза': '0474838458',
    'Сергій': '0550404033'
}

# print(contacts['Ліза'])
# contacts['Сергій'] = '0650499596'
# print(contacts['Сергій'])

# contacts['Настя'] = '0500440405'
# print(contacts['Настя'])

# contacts.update({'Антон': '0670450044', 'Тимофій': '0897477744'})

for i in contacts:
    print(f'{i}: {contacts[i]}')
contacts_copy = contacts.copy()
contacts_copy['Тимур'] = '0560985342'
for i in contacts:
    print(f"{i}: {contacts[i]}")










# print(contacts)

# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())

contacts.pop('Антон')
print(contacts)
contacts.popitem()
contacts.clear()




# first = {'apple', 'mango', 'cherry', 'kiwi'}
# second = {'mango' , 'pamelo', 'kiwi', 'oreange'}

# frozen_food = frozenset(first | second)

# print(frozen_food)
# print(type(frozen_food))

# frozen_food.add('watermelon') # не будет работать

# sym_diff = first.symmetric_difference(second)
# sym_diff = first ^ second # оператор XOR
# print(sym_diff)
# first.symmetric_difference_update(second)

# difference = first.difference(second)
# difference = first - second
# print(difference)

# first.difference_update(second)

# intersection = first.intersection(second)
# intersection = first & second # оператор &
# first.intersection_update(second)

# print(intersection)

# union = first.union(second)
# union = first | second # оператор or
# print(union)
# print(first)
# print(second)









# my_set = set()
# my_set = set( ["apple", "cherry", "mango"] )

# my_set = { 'apple', 'cherry', 'mango', 'cherry'}

# print(my_set)
# print(type(my_set))

# print(my_set[0])
# my_set[1] = 'pamelo'

# print(len(my_set))

# ne_set = {True, 1 , 0 , False}
# print(len(ne_set))
# print(ne_set)

# for i in my_set:
#     print(i)

# print("apple" in my_set)
# print("apple" not in my_set)

# my_set.add('pamelo')
# print(my_set)
# my_set.update(['kiwi', 'orange'])
# print(my_set)

# my_set.remove('pamelo')
# my_set.discard('pamelo')
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.clear()
# print(my_set)

