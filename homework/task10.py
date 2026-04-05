class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def __str__(self):
        return f'Name: {self.name} {self.surname}\nAge: {self.age}'
    
    def add(self, grade):
        if grade == int(grade):
            self.grades.append(grade)
        else:
            print('Число має бути')

    def show(self):
        if not self.grades:
            print('Оцінок немає')
        else: 
            print('Оцінки:', self.grades)




class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year


    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'

    def Show(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nШвидкість: {self.speed}\nРік: {self.year}")





def menu():
    while True:
        print("1 створити студента")
        print("2 додати оцінку студенту")
        print("3 показати оцінки студента")
        print("4 створити авто")
        print("5 показати авто")
        print("0 вихід")

        choice = input('? ')

        match choice:
            case 1:
                name = input("Ім’я: ")
                surname = input("Прізвище: ")
                age = int(input("Вік: "))
                student = Student(name, surname, age)
                print("Студента створено")
            case 2: 
                if student:
                    grade = int(input("Оцінка: "))
                    student.add(grade)
                else:
                    print("Нема")
            case 3: 
                if student:
                    print(student)
                    student.show()
                else:
                    print("Нема")
            case 4:
                brand = input("Бренд: ")
                model = input("Модель: ")
                speed = input("Швидкість: ")
                year = input("Рік: ")
                car = Car(brand, model, speed, year)
                print("Авто створено")
            case 5: 
                if car:
                    print(car)
                    car.Show()
                else:
                    print("Нема")
            case 0:
                break
             
menu()




