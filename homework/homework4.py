# angl = {
#     "apple": "яблуко",
#     "dog": "собака",
#     "cat": "кіт",
#     "house": "будинок",
#     "car": "автомобіль"
# }
# word = input("англійське слово: ").lower()
# if word in angl:
#     print(angl[word])
# else:
#     print("нема")


c = int(input("Кількість людейЖ "))
games = set(input('Введіть ігри: ').split(', '))
games3 = games.copy()
for i in range(c):
    games1 = set(input('Введіть ігри: ').split(', '))
    games3 = games1 & games3
if games3:
    print(games3)
else:
    print('нема')








