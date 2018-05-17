# encoding: utf-8
#! /usr/bin/env python

from treasure_hunts import MAP, map2list, search_treasre
from generate_treasure import generate_map
import turtle


def draw_map(lis, route):
    turtle.hideturtle()
    lis = lis[:]
    lis.reverse()
    width = len(lis[0])
    height = len(lis)

    space = 80

    turtle.up()
    # Draw map
    for row in range(height):
        for col in range(width):
            turtle.goto(col * space - width * space / 2,
                        row * space - height * space / 2)
            turtle.write(lis[row][col], False,
                         align="left", font=("Arial", 12, "normal"))

    route = [int(cell) for cell in route]
    route = [(height - (cell / 10) + 1, cell % 10)
             for cell in route]

    turtle.pencolor('red')
    ind = 1
    start_x, start_y = route[0]
    turtle.goto((start_y - 1) * space - width * space / 2,
                (start_x - 1) * space - height * space / 2)

    turtle.down()

    # Draw route
    for x, y in route:
        to_x = (y - 1) * space - width * space / 2
        to_y = (x - 1) * space - height * space / 2
        turtle.goto(to_x, to_y)
        turtle.dot()
        turtle.up()
        turtle.goto(to_x - space / 4, to_y + space / 4)
        turtle.write(str(ind), False,
                     align="left", font=("Arial", 10, "normal"))
        turtle.goto(to_x, to_y)
        turtle.down()
        ind += 1
    turtle.done()


if __name__ == "__main__":
    turtle.reset()
    MAP1 = generate_map(9, 7, 10)
    route = search_treasre(MAP1)
    draw_map(MAP1, route)
