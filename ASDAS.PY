import turtle

def draw_egg(t, color, width, height, x, y):
    # No creamos un turtle nuevo, usamos el que se pasa
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    
    t.begin_fill()
    t.setheading(45)
    for _ in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.end_fill()

def draw_triangle(t, color, size, x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_circle_outline(t, color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    
    t.color(color)
    t.fillcolor("")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Setup
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

# Dibujo huevos
draw_egg(t, "black", 300, 140, 50, -100)
draw_egg(t, "white", 190, 65, 0, -100)
draw_egg(t, "white", 60, 30, -70, 220)
draw_egg(t, "white", 40, 50, 30, 220)
draw_egg(t, "black", 10, 6, -15, 240)
draw_egg(t, "black", 15, 8, -65, 240)

# Dibujo pico (triángulo)
draw_triangle(t, "orange", 15, -35, 200, heading=0)

t.hideturtle()
turtle.done()
