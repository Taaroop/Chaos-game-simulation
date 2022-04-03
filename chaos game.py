import turtle
import random

length = 400
width = 400
iterations = 10000
d = 1/2

def draw_chaos_game(length, width, iterations, d):
    turtle.speed(0)
    turtle.penup()

    p1 = [random.randrange(length), random.randrange(width)]
    p2 = [random.randrange(length), random.randrange(width)]
    p3 = [random.randrange(length), random.randrange(width)]

    li_ini = [p1, p2, p3]

    for p in li_ini:
        turtle.goto(p[0], p[1])
        turtle.dot(5, 'black')

    p_seed = [random.randrange(length), random.randrange(width)]

    for i in range(iterations):
        roll = random.randint(0, 2)
        li_p = [p1, p2, p3]
        point = li_p[roll]
        x_destination = (p_seed[0] + point[0]) * (d)
        y_destination = (p_seed[1] + point[1]) * (d)
        turtle.goto(x_destination, y_destination)
        turtle.dot(4, 'blue')
        p_seed = [turtle.xcor(), turtle.ycor()]

    return None

draw_chaos_game(length, width, iterations, d)
turtle.mainloop()
