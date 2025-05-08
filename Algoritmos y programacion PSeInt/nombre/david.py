import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
t.pensize(2)
t.speed(0)

# Animación de círculos giratorios
for i in range(6):
    for colors in ["orange", "orange", "orange", "orange", "orange", "orange"]:
        t.color(colors)
        t.circle(100)
        t.left(10)

for i in range(6):
    for colors in ["red", "red", "red", "red", "red", "red"]:
        t.color(colors)
        t.circle(50)
        t.left(10)

t.speed(10)
t.pensize(10)

# Dibujo del nombre "DAVID"
turtle.title("Nombre: DAVID")

# D
t.color("grey")
t.penup()
t.goto(-320, -90)
t.pendown()
t.left(90)
t.fd(140)
t.right(90)
t.circle(-70, 180)

# A
t.color("grey")
t.penup()
t.goto(-150, -90)
t.pendown()
t.right(90 - 25) 
t.fd(150)
t.right(130)
t.fd(150)
t.penup()
t.left(160)
t.fd(40)
t.left(85)
t.fd(15)
t.pendown()
t.fd(90)

# V
t.color("grey")
t.penup()
t.goto(100, -90)
t.pendown()
t.right(160)
t.fd(140)
t.left(120)
t.fd(150)

# I
t.color("grey")
t.penup()
t.goto(220, -90)
t.setheading(90)
t.pendown()
t.fd(140)

# D
t.color("grey")
t.penup()
t.goto(310, -90)
t.setheading(90)
t.pendown()
t.fd(140)
t.right(90)
t.circle(-70, 180)

t.hideturtle()
turtle.done()