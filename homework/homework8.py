# line = input('рядок: ')
# line1 = input('рядок: ')
# line2 = input('рядок: ')
# with open('file.txt', 'w') as file:
#     file.write(line + '\n')
#     file.write(line1 + '\n')
#     file.write(line2 + '\n') 





# file = open("log.txt", "r")
# text = file.read()
# file.close()
# words = text.lower().split()
# word_count = {}
# for word in words:
#     word = word.strip(".,!?;:\"()[]{}")
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# top_10 = sorted_words[:10]

# out = open("word_stats.txt", "w")

# for word, count in top_10:
#     out.write(word + " - " + str(count) + "\n")

# out.close()



def add_order():
    num = input("Номер замовлення: ")
    name = input("Назва товару: ")
    qty = input("Кількість: ")
    price = input("Ціна: ")

    file = open("orders.txt", "a")
    file.write(num + "," + name + "," + qty + "," + price + "\n")
    file.close()

    print("Замовлення додано")


def show_orders():
    try:
        file = open("orders.txt", "r")
        print("\nСписок замовлень:")
        print(file.read())
        file.close()
    except:
        print("Файл ще не створений")


def find_order():
    num = input("Введіть номер: ")
    file = open("orders.txt", "r")

    found = False
    for line in file:
        data = line.strip().split(",")
        if data[0] == num:
            print("Знайдено:", data)
            found = True

    file.close()

    if not found:
        print("Не знайдено")


def update_order():
    num = input("Номер для оновлення: ")

    file = open("orders.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("orders.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == num:
            print("Старі дані:", data)
            data[2] = input("Нова кількість: ")
            data[3] = input("Нова ціна: ")
            line = ",".join(data) + "\n"

        file.write(line)

    file.close()
    print("Оновлено")


def delete_order():
    num = input("Номер для видалення: ")

    file = open("orders.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("orders.txt", "w")

    for line in lines:
        data = line.strip().split(",")
        if data[0] != num:
            file.write(line)

    file.close()
    print("Видалено (якщо існувало)")



while True:
    print("\n1 - Додати")
    print("2 - Показати всі")
    print("3 - Пошук")
    print("4 - Оновити")
    print("5 - Видалити")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        show_orders()
    elif choice == "3":
        find_order()
    elif choice == "4":
        update_order()
    elif choice == "5":
        delete_order()
    elif choice == "0":
        break
    else:
        print("Невірний вибір")





