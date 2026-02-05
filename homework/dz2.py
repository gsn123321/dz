size = int(input("розмір фігури: "))

print("Меню: \nа фігура \nб фігура \nв фігура \nг фігура \nд фігура \nе фігура \nж фігура \nз фігура \nи фігура \nк фігура")

figura = input("фігура: ")

if figura == "а":
    for i in range(size):
        print("*" * (size - i))

elif figura == "б":
    for i in range(size):
        print(" " * i + "*" * (size - i))

elif figura == "в":
    for i in range(size):
        print(" " * i + "*" * (size - 2 * i))

elif figura == "г":
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

elif figura == "д":
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

elif figura == "е":
    for i in range(size):
        for j in range(size):
            if j == i or j == size - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

elif figura == "ж":
    for i in range(size):
        print("*" * (i + 1))
    for i in range(size - 2, -1, -1):
        print("*" * (i + 1))

elif figura == "з":
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (i + 1))
    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + "*" * (i + 1))

elif figura == "и":
    for i in range(size):
        for j in range(size):
            if i + j >= size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

elif figura == "к":
    for i in range(size):
        for j in range(size):
            if i >= j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

else:
    print("неа")














































