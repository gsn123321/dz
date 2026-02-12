# text = input(": ")
# counter = 0
# for i in text:
#     if i == ".":
#         counter+=1
# print(counter)

# text = input(": ")
# text_striped = text.strip().lower()
# reversed_t = text_striped[::-1]
# if text_striped == reversed_t:
#     print('yeah')
# else:
#     print("no")

# text = input(": ")
# word = "ящерица"
# for word in text:
#     text1 = text.replace("ящерица", "ЯЩЕРИЦА")
# print(text1)

# text = input(": ")
# c1 = input(": ")
# c2 = input(": ")
# p1 = text.find(c1)
# p = text.find(c2)
# if 0 <= p1 < p:
#     result = text[:p1] + text[p+1:]
# else:
#     result = text
# print(result)

# text = input(": ")
# sym = input(": ")
# words = text.split()
# for i in words:
#     for j in sym:
#         if j in i:
#             text = text.replace(i, "")
#             break
# print(text.split())

text = input(": ")
text_rev = text.split()[::-1]
text1 = " ".join(text_rev)
print(text1)

