# number1 = int(input("число: "))
# number2 = int(input("степінь: "))

# match number2:
#     case 1:
#         print(f"{number1 ** 1}")
#     case 2:
#         print(f"{number1 ** 2}")
#     case 3:
#         print(f"{number1 ** 3}")
#     case 4:
#         print(f"{number1 ** 4}")
#     case 5:
#         print(f"{number1 ** 5}")
#     case 6:
#         print(f"{number1 ** 6}")
#     case 7:
#         print(f"{number1 ** 7}")
#     case _:
#         print("ашибка")

# number1 = int(input("число: "))

# if number1 > 100 or number1 < 0:
#     print("error")
# else:
#     if number1 % 3 == 0 and number1 % 5 > 0:
#         print("Fizz")
#     elif number1 % 3 > 0 and number1 % 5 == 0:
#         print("Buzz")
#     elif number1 % 3 == 0 and number1 % 5 == 0:
#         print("Fizz Buzz")
#     elif number1 % 3 > 0 and number1 % 5 > 0:
#         print(number1)
#     else:
#         print("error")

snack = input("закуска (салат/суп): ").lower()
main = input("основна страва (курка/риба): ").lower()
dessert = input("десерт (морозиво/фрукти): ").lower()
regular = input("ви постійний клієнт? (так/ні): ").lower()
total = 0

if snack == "салат":
    total += 5
elif snack == "суп":
    total += 7
if main == "курка":
    total += 10
elif main == "риба":
    total += 12
if dessert == "морозиво":
    total += 3
elif dessert == "фрукти":
    total += 4
discount = 0
discount = 0.10
if total > 20:
    discount = 0.15
if regular == "так":
    discount += 0.05
if snack == "суп" and main == "риба":
    print("знижка 2$ на десерт")
    total -= 2
if main == "курка" and dessert == "морозиво":
    print("компотик за рахунок закладу")
final_price = total * (1 - discount)
print(f"Підсумкова вартість: {final_price:.2f}$")

