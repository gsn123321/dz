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






day = int(input("номер дня тижня: "))



match day:
    case 1: print("понеділок")
    case 2: print("вівторок")
    case 3: print("сіріда")
    case 4: print("четверг")
    case 5: print("п/'ятниця")
    case 6: print("суббота")
    case 7: print("неділя")




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






