# numbers = input("числа через пробіл: ").split()
# n = int(input("кількість позицій: "))

# numbers2 = numbers[-n:] берет все последние  + numbers[:-n] берет все кроме последних

# print(numbers2)


import random

list1 = []
list2 = []

for i in range(10):
    list1.append(random.randint(1, 20))
    list2.append(random.randint(1, 20))

list3 = list1 + list2
print(list3)

list4 = []
for num in list3:
    if num not in list4: # not in проверяет нету ли его в списке
        list4.append(num)
print(list4)

list4 = []
for num in list1:
    if num in list2 and num not in list4:
        list4.append(num)
print(list4)

list4 = []
for num in list1:
    if num not in list2:
        list4.append(num)
for num in list2:
    if num not in list1:
        list4.append(num)
print(list4)

list4 = [min(list1), max(list1), min(list2), max(list2)] # min находит самое маленькое max самое большое 
print(list4)


















