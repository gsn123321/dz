
# with open("data.txt", "w") as file:
#     file.write("hello world\n")
# try:
#     with open("data.txt", "r") as s:
#         text = s.read()
#     with open("backup.txt", "w") as t:
#         t.write(text)  
# except Exception:
#     print('помилка')



with open('data.txt', 'w') as file:
    file.write('abcdef') 
def letter(a):
    if 'a' <= a <= 'z':
        return 'a' if a == 'z' else chr(ord(a) + 1)
    elif 'A' <= a <= 'Z':
        return "A" if a == 'Z' else chr(ord(a) + 1)
    else:
        return a
try: 
    with open('data.txt', 'r') as file:
        text = file.read()
    letters = ''.join(letter(i) for i in text)
    with open('encrypted.txt', 'w') as file:
        file.write(letters)
except Exception:
    print('помилка')        