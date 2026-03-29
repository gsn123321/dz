import turtle as t
# t.pencolor('red')
# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# t.penup()
# t.forward(200)
# t.pendown()
# t.pencolor('blue')
# for _ in range(3):
#     t.forward(100)
#     t.left(120)


# t.penup()
# t.forward(200)
# t.pendown()
# t.pencolor('green')
# for _ in range(5):
#     t.forward(50)
#     t.left(72)

# t.done()

# t.shape('turtle')
# t.fillcolor('red')
# t.begin_fill()
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()
# t.penup()
# t.goto(-70,100)
# t.pendown()
# t.fillcolor('blue')
# t.begin_fill()
# for _ in range(3):
#     t.forward(240)
#     t.left(120)
# t.end_fill()
# t.done()


import random as r
colors = ['red', 'blue', 'green', 'yellow', 'black']
t.pensize(5)
for _ in range(36):
    for _ in range(4):
        t.forward(100)
        t.pencolor(r.choice(colors))
        t.left(90)
    t.left(10)
t.done()
