import turtle

def dibujar_hexagono():
    for i in range(6):
        turtle.forward(50)
        turtle.left(60)

def dibujar_panal():
    for i in range(6):        
        dibujar_hexagono()
        turtle.forward(50)
        turtle.right(60)
        


turtle.speed(0)
turtle.shape('turtle')
turtle.pensize(5)
turtle.color('orange','lightyellow')
turtle.begin_fill()
dibujar_panal()
turtle.end_fill()
turtle.penup()
turtle.goto(-165,-176)
turtle.pendown()
turtle.begin_fill()
dibujar_panal()
turtle.end_fill()
turtle.done()