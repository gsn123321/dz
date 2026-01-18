'''
a = 2
b = 1

#if a > b: print("a більше b")
#10 + 11 - бінарний оператор
#num = -10
#-num - унарний оператор 

age = 17
#can_vote = age >= 18 ? True : False
print("a більше b") if a > b else print("a меньше b") if a < b else print("a дорівнює b")


login = input("Логін: ")
display_name = login if login else 'гість'
print(f'Привіт, {display_name}')

age = 17
if age < 18:
    pass # TODO: Implement underage logic later 
else:
    print("Full access granted")
'''






# day = int(input("номер дня тижня: "))



# match day:
#     case 1: print("понеділок")
#     case 2: print("вівторок")
#     case 3: print("сіріда")
#     case 4: print("четверг")
#     case 5: print("п/'ятниця")
#     case 6: print("суббота")
#     case 7: print("неділя")
#     case _: print("ашибка")

month = int(input("month: "))
day = int(input("номер дня тижня: "))

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 12:
        print("будній в грудні")
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("будній в січні")
    case 6 | 7 if month == 12:
        print("вихідний день в грудні")
    case 6 | 7 if month == 1:
        print("вихідний в січні")






# match month:
#     case 12 | 1 | 2: print("зима")
#     case 3 | 4 | 5: print("весна")
#     case 6 | 7 | 8: print("літо")
#     case 9 | 10| 11: print("осінь")
#     case _: print("неа")

# if day == 1:
#     print("понеділок")
# elif day == 2:
#     print("вівторок")
# elif day == 3:
#     print("сіріда")
# elif day == 4:
#     print("четверг")
# elif day == 5:
#     print("п/'ятниця")
# elif day == 6:
#     print("суббота")
# elif day == 7:
#     print("неділя")
# else:
#     print('error')






