# encoding : utf-8
#! /usr/bin/env python

import random
from treasure_hunts import draw_route
from treasure_hunts import map2list
from treasure_hunts import search_treasre
from treasure_hunts import report_map


def generate_route(width=5, height=5, length=10):
    route = ['11']
    cells = 0
    while cells <= length - 2:
        randomx = str(random.choice(range(height)) + 1)
        randomy = str(random.choice(range(width)) + 1)
        cell = randomx + randomy
        if cell in route:
            continue
        else:
            route.append(cell)
            cells += 1

    route.append(route[-1])
    return route


def generate_map(width=5, height=5, length=10):
    assert width < 10
    assert height < 10
    res = []
    for _ in range(height):
        line = []
        for _ in range(width):
            line.append('0')
        res.append(line)
    route = generate_route(width, height, length)
    for i in range(len(route) - 1):
        res[int(route[i][0]) - 1][int(route[i][1]) - 1] = route[i + 1]

    for x in range(height):
        for y in range(width):
            if res[x][y] == '0':
                randomx = str(random.choice(range(height)) + 1)
                randomy = str(random.choice(range(width)) + 1)
                res[x][y] = randomx + randomy

    return res


if __name__ == "__main__":
    MAP1 = generate_map(4, 3, 3)
    report_map(MAP1)
    draw_route(search_treasre(MAP1))
    print "----------------"

    MAP2 = generate_map(6, 7, 13)
    report_map(MAP2)
    draw_route(search_treasre(MAP2))
    print "----------------"

    MAP3 = generate_map(2, 7, 5)
    report_map(MAP3)
    draw_route(search_treasre(MAP3))
    print "----------------"
