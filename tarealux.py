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
        t.right(120)
    t.end_fill()

def draw_triangle_left(t, color, size, x, y, heading=0):
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

#def draw_egg(t, color, width, height, x, y):
def draw_right_triangle(t, color, size, x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    # Dibuja el triángulo rectángulo (ángulo de 90°)
    for _ in range(2):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_left_triangle(t, color, size, x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    # Dibuja el triángulo rectángulo, pero gira a la derecha (ángulo 90° hacia el otro lado)
    for _ in range(2):
        t.forward(size)
        t.left(280)
        
    t.end_fill()

# Setup
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

draw_egg(t, "black", 300, 140, 50, -100)
draw_egg(t, "gray", 190, 130, 50, -100)
draw_egg(t, "white", 200, 65, 0, -100)
draw_egg(t, "white", 60, 30, -70, 220)
draw_egg(t, "white", 40, 50, 30, 220)
draw_egg(t, "black", 10, 6, -15, 240)
draw_egg(t, "black", 15, 8, -65, 240)

draw_triangle(t, "orange", 75, -80, 210, heading=0)
draw_right_triangle(t, "black", 105, -295, 65, heading=0)
draw_left_triangle(t, "black", 105, 95, 100, heading=0)

draw_egg(t, "orange", 40, 80, -100, -160)
draw_egg(t, "orange", 40, 80, 60, -160)


t.hideturtle()
turtle.done()
