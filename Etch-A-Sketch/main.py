from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def clockwise():
    t.right(10)

def counter_clockwise():
    t.left(10)




screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkeypress(key = "d", fun = clockwise)
screen.onkeypress(key = "a", fun = counter_clockwise)
screen.onkey(key = "c", fun = screen.reset)



screen.exitonclick()