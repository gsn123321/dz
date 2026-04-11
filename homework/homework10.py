class Book:
    def __init__(self, title, authors, age):
        self.age = age
        self.authors = authors
        self.title = title

    def __str__(self):
        return f'Навза: {self.title}\nАвтори: {self.authors}\nРік: {self.age}'
    
class Library:
    def __init__(self, name, adres):
        self.name = name
        self.adres = adres
        self.book = []

    def __str__(self):
        return f'Бібліотека: {self.name}\nАдреса: {self.adres}\nКниг: {len(self.book)}'
    
    def books(self):
        if not self.book:
            print('Кинг немає')
        else:
            for i in self.book:
                print(i)

    def add(self, book):
        self.book.append(book)
        print('Додано')

    def remove(self, title):
        for i in self.book:
            if i.title.lower() == title.lower():
                self.book.remove(i)
                print('Книгу видалено')
                return
        print('Книгу не знайдено')

    def find(self, title):
        for i in self.book:
            if title.lower() in i.title.lower():
                print(i)
                return
        print('Книгу не знайдено')

    def find2(self, author):
        for i in self.book:
            if author in i.authors:
                print(i)
                return
        print('Автора не знайдено')

library = Library("Моя бібліотека", "м. Одеса")

        
def menu():
    while True:
        print("1 Показати всі книги")
        print("2 Додати книгу")
        print("3 Видалити книгу")
        print("4 Пошук за назвою")
        print("5 Пошук за автором")
        print("0 Вихід")

        choice = input("? ")

        if choice == "1":
            library.books()

        elif choice == "2":
            title = input("Назва: ")
            authors = input("Автори: ").split(",")
            year = input("Рік: ")


            book = Book(title, authors, year)
            library.add(book)
        
        elif choice == "3":
            title = input("Введіть назву книги для видалення: ")
            library.remove(title)

        elif choice == "4":
            title = input("Введіть назву для пошуку: ")
            library.find(title)

        elif choice == "5":
            author = input("Введіть автора: ")
            library.find2(author)
        
        elif choice == "0":
            break

        else:
            print("Error")
        

menu()











