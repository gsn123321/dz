# contacts = {}
# while True:
#     print('0) виход')
#     print("1) додати контакт")
#     print("2) видалити контакт")
#     print("3) змінити контакт")
#     print("4) показати всі контакти")
#     w = input("число: ")
    
#     if w == "1":
#         name = input("ім'я: ")
#         phone = input("номер телефону: ")
#         contacts[name] = phone
#         print("додано")
#     elif w == "2":
#         name = input("ім'я: ")
#         if name in contacts:
#             contacts.pop(name)
#             print("видалено")
#         else:
#             print("не знайдено")
#     elif w == "3":
#         name = input("ім'я: ")
#         if name in contacts:
#             phone = input("новий номер: ")
#             contacts[name] = phone
#             print("змінено")
#         else:
#             print("не знайдено")
#     elif w == "4":
#         if contacts:
#             print("список контактів:")
#             print(contacts)
#         else:
#             print("порожньо")
#     elif w == "0":
#             break
#     else:
#         print("чет не то")



# text = input("Введіть текст: ")
# words = text.split()
# word = []

# for i in words:
#     if i not in word:
#         word.append(i)

# for i in word:
#     print(i, ":", words.count(i))



# rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

# c = input("USD, EUR, PLN: ").upper()
# a = float(input("суму в гривнях: "))

# if c in rates:
#     r = a / rates[c]
#     print(f"{r} {c}")
# else:
#     print("немає")


angl = {
    "apple": "яблуко",
    "dog": "собака",
    "cat": "кіт",
    "house": "будинок",
    "car": "автомобіль"
}
word = input("англійське слово: ").lower()
if word in angl:
    print(angl[word])
else:
    print("нема")






