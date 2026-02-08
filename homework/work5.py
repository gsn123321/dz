# side = int(input('Введіть довжину сторони: '))
# symbol = input('Введіть символ: ')

# for i in range(1, side // 2 + 1):
#     for j in range(1, side // 2 + 1):
#         if j < i:
#             print(symbol, end='')
#         else:
#             print(' ', end='')

#     for j in range(side // 2, 0, -1):
#         if j < i:
#             print(symbol, end='')
#         else:
#             print(' ', end='')
#     print()

# for i in range(1, side // 2 + 1):
#     for j in range(side // 2, 0, -1):
#         if j < i:
#             print(' ', end='')
#         else:
#             print(symbol, end='')

#     for j in range(1, side // 2 + 1):
#         if j < i:
#             print(' ', end='')
#         else:
#             print(symbol, end='')
#     print()


# print(text[0])
# print(text[8])
# print(text[3:7])
# print(text[:7])
# print(text[7:])
# print(text[1:3:1])
# print(text[-1])
# print(text[-1:-10:-1])
# print(text[::-1])

# side = int(input('Введіть довжину сторони: '))
# symbol = input('Введіть символ: ')

# symbols = 1
# spaces = side - symbols * 2

# for i in range(side + 1):
#     for j in range(side):
#         if j < symbols or j > side - symbols - 1:
#             print(symbol, end='')
#         else:
#             print(' ', end='')
#     symbols += 1 if i < side // 2 else -1
#     spaces = side - symbols * 2
#     print()
# text = 'textt'
# print(len(text))

# counter = 0 
# while counter < len(text):
#     print(text[counter], end=' ')
#     counter+=1
# print()

# for symbol in text:
#     print(symbol, end=" ")
# text_lower = text.lower()
# text_upper = text.upper()
# print(text_lower)
# print(text_upper)
# print(text)

# text_stripped = text.strip()
# print(text_stripped)
# print(text)

# words = text.split(', ')
# modified = text.replace("l", "c")
# modified2 = text.replace("world", "Python")

# print(modified)
# print(modified2)
# print(text)
# print(words)
# print(words[1])
# if text.startswith('Hello'):
#     print('Це привітання!')

# if text.endswith("!"):
#     print("Це вигук")

# print("lemon">"apple")
# print("h">"H")

# text = '\tHello world!    \n '
# text = text.strip()

# fruit = input(": ")
# if fruit != "apple":
#     print("apple")

# print("a" in "apple")
# print("b" in "apple")

# if "a" in "apple":
#     print("a in apple")
# print(text * 3)
# part1 = "Hello"
# part2 = "Python"

# result = part1 + ", " + part2
# print(result)

# 1 bit = 0 or 1
# 0 0 0 0 0 0 0 0

# print(2 ** 8)
# print(2 ** 7)

# text = "Hello, world"
# encoded = text.encode("utf-16")
# print(encoded)

# decoded = encoded.decode("utf-16") 
# print(deco)


# str.isalnum() — перевіряє, чи рядок str складається тільки з літер та цифр
# str.isalpha() — перевіряє, чи рядок str складається лише з літер.
# str.isdigit() — перевіряє, чи рядок str складається лише з цифр.
# str.islower() — перевіряє, чи всі літери рядка str в нижньому регістрі (не літери ігноруються).
# str.isupper() — перевіряє, чи всі літери рядка str в верхньому регістрі (не літери ігноруються).
# str.isspace() — перевіряє, чи до складу рядка str входять лише пробіли (пробіл, табуляція (\t), перехід на новий рядок (\n)).
# str.istitle() — перевіряє, чи починається кожне слово рядка str із символу у верхньому регістрі.

