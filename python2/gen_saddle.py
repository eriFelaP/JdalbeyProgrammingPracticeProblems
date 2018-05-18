# encoding: utf-8
#! /usr/bin/env python

import random
from saddle_points import get_saddle_point
from treasure_hunts import report_map


def gen_saddle(nrow=5, ncol=5):
    res = gen_none_array(nrow, ncol)

    saddle_point = random.randint(0, 100)

    res[0][0] = saddle_point

    for i in range(1, ncol):
        res[0][i] = random.randint(0, saddle_point)
    for i in range(1, nrow):
        res[i][0] = random.randint(saddle_point, 100)

    for x in range(1, ncol):
        for y in range(1, nrow):
            res[y][x] = random.randint(0, 100)
    random.shuffle(res)
    res = transpose(res)
    random.shuffle(res)
    res = transpose(res)
    return res


def gen_none_array(nrow, ncol):
    res = []
    for _ in range(nrow):
        row = []
        for _ in range(ncol):
            row.append(None)
        res.append(row)
    return res


def transpose(array):
    nrow = len(array)
    ncol = len(array[0])
    res = gen_none_array(ncol, nrow)
    for y in range(nrow):
        for x in range(ncol):
            res[x][y] = array[y][x]
    return res


if __name__ == "__main__":
    array = gen_saddle(6, 5)
    report_map(array)
    print "--------------"
    print get_saddle_point(array)
