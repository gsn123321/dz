
# with open("data.txt", "w") as file:
#     file.write("hello world\n")
# try:
#     with open("data.txt", "r") as s:
#         text = s.read()
#     with open("backup.txt", "w") as t:
#         t.write(text)  
# except Exception:
#     print('помилка')



# with open('data.txt', 'w') as file:
#     file.write('abcdef') 
# def letter(a):
#     if 'a' <= a <= 'z':
#         return 'a' if a == 'z' else chr(ord(a) + 1)
#     elif 'A' <= a <= 'Z':
#         return "A" if a == 'Z' else chr(ord(a) + 1)
#     else:
#         return a
# try: 
#     with open('data.txt', 'r') as file:
#         text = file.read()
#     letters = ''.join(letter(i) for i in text)
#     with open('encrypted.txt', 'w') as file:
#         file.write(letters)
# except Exception:
#     print('помилка')      


FILENAME = "music_collection.txt"

def add_album():
    title = input("Введіть назву альбому: ")
    artist = input("Введіть виконавця: ")
    year = input("Введіть рік випуску: ")

    file = open(FILENAME, "a")
    file.write(title + "|" + artist + "|" + year + "\n")
    file.close()
    print("Альбом додано!")

def view_collection():
    try:
        file = open(FILENAME, "r")
        lines = file.readlines()
        file.close()
        if len(lines) == 0:
            print("Колекція порожня.")
            return
        print("\nВаша музична колекція:")
        for i, line in enumerate(lines, start=1):
            title, artist, year = line.strip().split("|")
            print(str(i) + ". " + title + " — " + artist + " (" + year + ")")
        print()
    except:
        print("Колекція порожня.")

def search_by_artist():
    try:
        artist_search = input("Введіть ім'я виконавця для пошуку: ").lower()
        file = open(FILENAME, "r")
        lines = file.readlines()
        file.close()
        found = False
        for line in lines:
            title, artist, year = line.strip().split("|")
            if artist_search in artist.lower():
                print(title + " — " + artist + " (" + year + ")")
                found = True
        if not found:
            print("Альбомів цього виконавця не знайдено.")
    except:
        print("Колекція порожня.")

def delete_album():
    try:
        title_search = input("Введіть назву альбому для видалення: ").lower()
        file = open(FILENAME, "r")
        lines = file.readlines()
        file.close()

        found = False
        file = open(FILENAME, "w")
        for line in lines:
            title, artist, year = line.strip().split("|")
            if title_search != title.lower():
                file.write(line)
            else:
                found = True
        file.close()

        if found:
            print("Альбом видалено!")
        else:
            print("Альбом не знайдено.")
    except:
        print("Колекція порожня.")

def main():
    while True:
        print("\nМузична колекція — меню:")
        print("1. Додати новий альбом")
        print("2. Переглянути всю колекцію")
        print("3. Пошук альбомів за виконавцем")
        print("4. Видалити альбом")
        print("5. Вихід")

        choice = input("Оберіть дію (1-5): ")

        if choice == "1":
            add_album()
        elif choice == "2":
            view_collection()
        elif choice == "3":
            search_by_artist()
        elif choice == "4":
            delete_album()
        elif choice == "5":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()











