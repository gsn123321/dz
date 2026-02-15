'''
collection = list() # функція конструктор
collection = [] # пустий список

print(type(collection))

collection = [10, 12.5 , 'text' , True] # погана практика

# print(collection[0].upper())



# list[start:end:step]

print(fruits[0])
print(fruits[1:3])
print(fruits[1:])
print(fruits[:4])

print(fruits[-1])
print(fruits[-1:-5:-1])
print(fruits[::-1])

# text = 'text'
# text[2]= 'u'
fruits[3] = 'kiwi' # манго на киви
print(fruits)

fruits_count = len(fruits)
print(fruits_count)

counter = 0
while counter < len(fruits):
    print(fruits[counter].upper())
    counter += 1


for fruit in fruits:
    print(fruit)

names = input("Введіть імена через кому: ")
names = names.split(", ")
print(names)
print(type(names))
'''
fruits = ['apple', 'lemon',  'pamelo', 'mango', 'pineapple']

# # print(", ".join(fruits))
# fruits.append('kiwi')
# # print(", ".join(fruits))
# fruits.extend(["orange", 'banana'])
# # print(", ".join(fruits))
# fruits.insert(3, 'watermelon')
# # print(", ".join(fruits))

# tuple1 = tuple()
# print(type(tuple1))

# fruits_tuple = tuple(fruits)
# print(fruits_tuple)
# print(type(fruits_tuple))

# fruits_tuple[2] = 'jdnfskadf'

# fruits_tuple = tuple(['apple', 'orange'])
# print(fruits_tuple)

colors = ("red", "blue", "green", "purple")
(red, green, blue, purple) = colors
(red, green, *other_colors) = colors
print(other_colors)
print(red)
print(green)
print(blue)
print(purple)

# list2d = [ [1,2,3], [4 , 5, 6]]

# for list in list2d:
#     for i in list:
#         print(i, end=" ")
#     print()

# new_list = [вираз for змінна in  послідовності if умова]

# numbers = [10, 1 ,2 ,3 ,-6 ,0, -11, 5]
# even_numbers = [number for number in numbers if number % 2 == 0]
# # for number in numbers:
# #     if number % 2 ==0:
# #         even_numbers.append(number)

# print(even_numbers)

# odd_numbers = [x for x in range(1,20,2)]
# print(odd_numbers)


# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# list = [1,2,3,4]
# list2 = [5,6,7]
# result = list + list2
# print(result)


# apple_count = fruits.count('apple')
# print(apple_count)
# peach_counter = fruits.count('peach')
# print(peach_counter)

# while "watermelon" in fruits:
#     fruits.remove('watermelon')

# if "grapefruit" in fruits:
#     fruits.remove('grapefruit')

# print(fruits.index('pineapple'))
# print(fruits.index('grapefruit'))

# fruits_copy = fruits.copy()
# fruits_copy.append('grapefruit')
# print(fruits_copy)
# print(fruits)




# fruits.pop(5)
# print(", ".join(fruits))
# fruits.remove('watermelon')
# print(", ".join(fruits))
# fruits.clear()
# print(fruits)
# print(len(fruits))














