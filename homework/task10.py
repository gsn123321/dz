# class Student:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = []

#     def __str__(self):
#         return f'Ім’я: {self.name} {self.surname}\nРік: {self.age}'
    
#     def add(self, grade):
#         if grade == int(grade):
#             self.grades.append(grade)
#         else:
#             print('Число має бути')

#     def show(self):
#         if not self.grades:
#             print('Оцінок немає')
#         else: 
#             print('Оцінки:', self.grades)




# class Car:
#     def __init__(self, brand, model, speed, year):
#         self.brand = brand
#         self.model = model
#         self.speed = speed
#         self.year = year


#     def __str__(self):
#         return f'{self.brand} {self.model} {self.year}'

#     def Show(self):
#         print(f"Бренд: {self.brand}\nМодель: {self.model}\nШвидкість: {self.speed}\nРік: {self.year}")





# def menu():
#     while True:
#         print("1 створити студента")
#         print("2 додати оцінку студенту")
#         print("3 показати оцінки студента")
#         print("4 створити авто")
#         print("5 показати авто")
#         print("0 вихід")

#         choice = int(input('? '))

#         match choice:
#             case 1:
#                 name = input("Ім’я: ")
#                 surname = input("Прізвище: ")
#                 age = int(input("Вік: "))
#                 student = Student(name, surname, age)
#                 print("Студента створено")
#             case 2: 
#                 if student:
#                     grade = int(input("Оцінка: "))
#                     student.add(grade)
#                 else:
#                     print("Нема")
#             case 3: 
#                 if student:
#                     print(student)
#                     student.show()
#                 else:
#                     print("Нема")
#             case 4:
#                 brand = input("Бренд: ")
#                 model = input("Модель: ")
#                 speed = input("Швидкість: ")
#                 year = input("Рік: ")
#                 car = Car(brand, model, speed, year)
#                 print("Авто створено")
#             case 5: 
#                 if car:
#                     print(car)
#                     car.Show()
#                 else:
#                     print("Нема")
#             case 0:
#                 break
             
# menu()





import math

class Circle:
    def __init__(self, r):
        self.r = r

    def s(self):
        return math.pi * self.r ** 2

    def p(self):
        return self.r * math.pi * 2
    
class Triangle:
    def __init__(self, a ,b ,c):
        self.a = a
        self.b = b
        self.c = c

    def p(self):
        return self.a + self.b + self.c
    
    def s(self):
        per = self.p() / 2
        return math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c))
           
class Rectangle:
    def __init__(self, a ,b):
        self.b = b
        self.a = a
    
    def s(self):
        return self.a * self.b
    
    def p(self):
        return (self.a + self.b) * 2
        

def menu():
    while True:
        print("1 Коло")
        print("2 Прямокутник")
        print("3 Трикутник")
        print("0 Вихід")

        choice = int(input("? "))

        match choice:
            case 1: 
                r = float(input("Введіть радіус: "))
                x = Circle(r)
                print("Площа:", x.s())
                print("Периметр:", x.p())
            case 2:
                a = float(input("Перша сторона: "))
                b = float(input("Друга сторона: "))
                x = Rectangle(a, b)
                print("Площа:", x.s())
                print("Периметр:", x.p())
            case 3: 
                a = float(input("Сторона 1: "))
                b = float(input("Сторона 2: "))
                c = float(input("Сторона 3: "))
                x = Triangle(a, b, c)
                print("Площа:", x.s())
                print("Периметр:", x.p())
            case 0:
                break
            case _: 
                print('Error')
menu()









