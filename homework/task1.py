# numbers = input("Введіть числа через пробел: ").split()
# counter = 0
# for num in numbers:
#     counter += int(num)
# s1 = counter / len(numbers)
# print(counter, s1)

# numbers = input(": ").split()
# number = int(input(": "))
# counter = 0
# for num in numbers:
#     if int(num) == number:
#         counter += 1
# print(counter)

# numbers = input(": ").split()
# counter = 0
# for num in numbers:
#     number = int(num)
#     counter += number
# print(counter)

# numbers = input(": ").split()
# for i in range(len(numbers)):
#     if int(numbers[i]) % 2 == 0:
#         print(i)

numbers = input(": ").split()
new = []
for i in numbers:
    if i not in new:
        new.append(i)
print(new)









