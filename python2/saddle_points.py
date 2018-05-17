# encoding: utf-8
#! /usr/bin/env python

import random
from treasure_hunts import report_map


def gen_array(nrow=5, ncol=5, max_limit=100):
    array = []
    for _ in range(nrow):
        row = []
        for _ in range(ncol):
            row.append(random.choice(range(max_limit)))
        array.append(row)
    return array


def get_max_in_row(array, nrow):
    return max(array[nrow])


def get_min_in_col(array, ncol):
    col = []
    for row in array:
        col.append(row[ncol])
    return min(col)


def get_saddle_point(array):
    res = []
    ncol = len(array[0])
    nrow = len(array)
    for x in range(ncol):
        for y in range(nrow):
            point = array[y][x]
            if point >= get_max_in_row(array, y) and \
               point <= get_min_in_col(array, x):
                res.append(point)
    return res


def main():
    array = gen_array()
    report_map(array)
    res = get_saddle_point(array)
    if len(res) == 0:
        print "No saddle points"
    else:
        print res


if __name__ == "__main__":
    main()
    array = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    print get_saddle_point(array)
