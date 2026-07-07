#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ Create a function that returns the perimeter
    of the island described in grid """

    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                # Check la case du dessus
                if row == 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                # Check la case du bas
                if row == rows - 1 or grid[row + 1][column] == 0:
                    perimeter += 1
                # Check la case de gauche
                if column == 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                # Check la case de droite
                if column == columns - 1 or grid[row][column + 1] == 0:
                    perimeter += 1

    return perimeter
