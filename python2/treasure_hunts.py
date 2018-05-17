# encoding: utf-8
#! /usr/bin/env python


import re
import turtle

MAP = """
+-------------------------+
¦ 34 ¦ 21 ¦ 32 ¦ 41 ¦ 25  ¦
+----+----+----+----+-----¦
¦ 14 ¦ 42 ¦ 43 ¦ 14 ¦ 31  ¦
+----+----+----+----+-----¦
¦ 54 ¦ 45 ¦ 52 ¦ 42 ¦ 23  ¦
+----+----+----+----+-----¦
¦ 33 ¦ 15 ¦ 51 ¦ 31 ¦ 35  ¦
+----+----+----+----+-----¦
¦ 21 ¦ 52 ¦ 33 ¦ 13 ¦ 23  ¦
+-------------------------+
"""


def map2list(tmap):
    lis = []
    for line in str.split(tmap, "\n"):
        clues = [clue for clue in re.findall("[0-9]+", line)]
        if len(clues) != 0:
            lis.append(clues)
    return lis


def next_clue(clue, lis):
    x = int(clue[0])
    y = int(clue[1])
    return lis[x - 1][y - 1]


def search_treasre(lis):

    clue = "11"
    route = ["11"]

    while clue != next_clue(clue, lis):
        clue = next_clue(clue, lis)
        route.append(clue)

    return route


def draw_route(route):
    res = "\n"
    ind = 0
    for rou in route:
        if ind >= 4:
            ind = 0
            res += "=>" + rou + "\n"
        else:
            ind += 1
            res += "=>" + rou
    print res


def report_map(lis):
    print "\n"
    for row in lis:
        line = "|"
        for col in row:
            line += " " + str(col) + " " + "|"
        print line


if __name__ == "__main__":
    lis = map2list(MAP)
    route = search_treasre(lis)
    report_map(lis)
    draw_route(route)
