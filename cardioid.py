"""
p. 15 from "This is not a math book"
"""

import turtle

RADIUS = 100
CENTER = (0, RADIUS)

s = turtle.getscreen()
t = turtle.Turtle()

t.circle(RADIUS)
t.penup()


t.goto(CENTER)
t.rt(90)

for i in range(18):
    t.rt(20)
    # t.fd(100)

    if i % 2 == 0:
        t.fd(100)
        # draw the smaller circle
        # catching the top point, zeroth

        if i < 9:
            small_radius = i * 40
            t.pendown()
            t.circle(small_radius)
        else:
            small_radius = (i - 9) * 40
            t.rt(90)
            t.pendown()
            t.circle(small_radius)
            t.rt(90)

    t.penup()
    t.goto(CENTER)


