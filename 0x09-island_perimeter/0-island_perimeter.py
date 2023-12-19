#!/usr/bin/python3
"""
The Island perimeter
"""


def island_perimeter(grid):
    """Finding the perimeter of the island
    """
    perim = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perim += 4
                if row > 0 and grid[row-1][col] == 1:
                    perim -= 2
                if col > 0 and grid[row][col-1] == 1:
                    perim -= 2
    return perim
