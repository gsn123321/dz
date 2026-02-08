# text = input(": ")
# l = 0
# s = 0
# for i in text:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         s+=1
# print(l , s)

# text = input(": ")
# symbol = input(": ")
# count = 0
# for i in text:
#     if i == symbol:
#         count+=1
# print(count)

# text = input(": ")
# print(text[::-1])

# text = input(": ")
# word = input(": ")
# count = text.count(word)
# print(count)

# text = input(": ")
# word = input(": ")
# word1 = input(": ")
# count = text.replace(word, word1)
# print(count)

text = input(": ")
words = text.split()
word1 = ""
for i in words:
    if len(i) > len(word1):
        word1 = i
print(word1)























