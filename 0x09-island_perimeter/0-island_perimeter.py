#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Island Perimeter"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4
                # Check if the cell above is land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Check if the cell to the left is land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
