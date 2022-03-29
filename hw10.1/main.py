# Code from : http://openbookproject.net/thinkcs/python/english3e/recursion.html
# Accessed on 22/03/2022
# Modified for full turtle draw


import turtle
def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def main():
    size = 300
    screen = turtle.Screen()
    screen.setup(size+20, size+20) #window size
    #if setup not larger than screensize, scrollbars will appear
    screen.screensize(size, size) #drawing space
    screen.bgcolor("yellow")
    screen.title(("Black turtle under Yellow"))

    turtle.penup( )
    turtle.goto(-size/2, 0)
    turtle.pendown()
    turtle.color("black")
    # turtle.pensize(10)

    for _ in range(3):
        koch(turtle, 3, 100)
        turtle.right(120)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.resizemode("user")
    turtle.shapesize(2, 2, 2)
    turtle.speed(50)

    #screen.exitonclick()
    screen.onclick(turtle.goto)

    #koch(turtle, 3, 100)

if __name__ == "__main__":
    main()
