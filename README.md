Some programming practice problems come from Dr. John Dalbey and some extension problems I add

  * [Programming Practice Problems](http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html)
  * [Dr. John Dalbey](http://users.csc.calpoly.edu/~jdalbey/)


# Easy Problems

## Problem 1

```

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

```

Do you like treasure hunts? In this problem you are to write a program to
explore the above array for a treasure. The values in the array are clues. Each
cell contains an integer between 11 and 55; for each value the ten's digit
represents the row number and the unit's digit represents the column number of
the cell containing the next clue. Starting in the upper left corner (at 1,1),
use the clues to guide your search of the array. (The first three clues are 11,
34, 42). The treasure is a cell whose value is the same as its coordinates. Your
program must first read in the treasure map data into a 5 by 5 array. Your
program should output the cells it visits during its search, and a message
indicating where you found the treasure.

**Solution:**

  * [Python 2](./python2/treasure_hunts.py)

## Extension 1-1

How to automatically generate a treasure map?

**Solution:**

  * [Python 2](./python2/generate_treasure.py)

## Extension 1-2

Draw the treasure map and route.

**Solution:**

  * [Python 2](./python2/draw_treasure_and_route.py)

## Problem 2

Write a program to search for the "saddle points" in a 5 by 5 array of integers.
A saddle point is a cell whose value is greater than or equal to any in its row,
and less than or equal to any in its column. There may be more than one saddle
point in the array. Print out the coordinates of any saddle points your program
finds. Print out "No saddle points" if there are none.

**Solution:**

  * [Python 2](./python2/saddle_points.py)

## Extension 2-1

Write a program to generate an array containing saddle points.

**Solution:**

  * [Python 2](./python2/gen_saddle.py)

# Moderate Problems
