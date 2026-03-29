# from random import randint
# from random import *
# import random as r # псевдоним

# print(r.randint(10,15))
# print(r.randint(10, 19, 2))
# print(r.random())
# print(r.uniform(-10.5, 10.5))

# fruits = ['apple', 'mango', 'banana', 'lemon', 'orange']
# print(r.choice(fruits))
# print(r.choice('hello'))
# print(r.choices(fruits, weights=[0.5, 0.1, 0.2, 0.05, 0.15], k=3))
# print(r.sample(fruits,k=4))

# fruits.sort()
# print(fruits)
# r.shuffle(fruits)
# print(fruits)

# import math as m

# print(m.pi)
# print(m.e)
# print(m.inf)
# m.log(10, 10)

# m.ceil(20.6)
# print(m.floor(20.6))
# print(m.trunc(20.6))

# print(m.fabs(-10.5))

# print(m.sqrt(9))
# print(m.factorial(5))

# print(m.gcd(10, 5))
# print(m.pow(10, 5))

# import string as s

# print(s.ascii_letters)
# print(s.ascii_letters)
# print(s.ascii_uppercase)

# print(s.digits)
# print(s.hexdigits)
# print(s.octdigits)
# print(s.punctuation)

# print(s.whitespace) # space \n \r \t

# print(s.printable)

import turtle as t
from turtle_config import *

t.shape(SHAPE)
t.pensize(PEN_SIZE)
# t.color("red")
# t.color("#2eff25")
t.color(COLOR)
t.fillcolor(FILL_COLOR)
t.speed(SPEED)

print_config()

# t.forward(100)
# t.right(80)
# t.forward(40)
# t.left(50)
# t.back(100)

# t.begin_fill()
# t.circle(25)
# t.end_fill()

# t.penup()
# t.goto(-100, 100)
# t.pendown()

# t.circle(150)

screen = t.Screen()

screen.onkey(lambda: t.forward(5), 'w')
screen.onkey(lambda: t.right(15), 'd')
screen.onkey(lambda: t.back(5), 's')
screen.onkey(lambda: t.left(15), 'a')
screen.onclick(lambda x, y: t.goto(x, y))

screen.listen()

t.done()





