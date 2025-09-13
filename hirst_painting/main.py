
import colorgram

import turtle as d
from turtle import Turtle, Screen
import random

# GET COLOR FROM HIRST'S DOT PAINTING
# rgb_colors = []
# colors = colorgram.extract('photo.jpg', 6)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


screen = Screen()
screen.title('Hirst Painting')
screen.setup(width = 750, height = 750)

cv = screen.getcanvas()
root = cv.winfo_toplevel()
root.resizable(False, False)

t = Turtle()
t.pensize(20)
d.colormode(255)

color_list = [(225, 212, 213), (225, 183, 212), (225, 231, 237), (202, 172, 110), (238, 245, 243), (154, 181, 196)]

start = -300
end = -300
t.teleport(start, end)
t.penup()

for i in range(0, 10):
    for j in range(0, 10):
        color = random.choice(color_list)
        t.dot(20, color)
        t.forward(50)
    end += 50
    t.teleport(start, end)


screen.exitonclick()