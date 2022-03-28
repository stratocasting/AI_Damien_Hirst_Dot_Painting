# import colorgram
# rgb_colors = []
# colors = colorgram.extract('damien_hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print (rgb_colors)
import turtle as turtle_module
from turtle import Screen
import random
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
damien = turtle_module.Turtle()
turtle_module.colormode(255)
damien.penup()
damien.speed(250)

damien.setheading(225)
damien.forward(250)
damien.setheading(0)

for x in range (10):
    for x in range (9):
        damien.dot(20, random.choice(color_list))
        damien.forward(50)

    damien.setheading(180)
    damien.forward(450)
    damien.setheading(90)
    damien.forward(50)
    damien.setheading(360)



Screen().exitonclick()
