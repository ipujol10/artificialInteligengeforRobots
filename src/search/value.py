# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def isValidCell(grid, x, y):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return False
    return grid[x][y] == 0


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    x, y = goal
    value = [[99 for _ in row] for row in grid]
    searching = [[0, x, y]]
    while (searching):
        nextUP = min(searching)
        searching.remove(nextUP)
        g, x, y = nextUP
        value[x][y] = g
        for dlt in delta:
            x2 = x - dlt[0]
            y2 = y - dlt[1]
            if (isValidCell(grid, x2, y2)):
                v2 = g + cost
                if (v2 < value[x2][y2]):
                    searching.append([v2, x2, y2])
    return value


if (__name__ == "__main__"):
    vals = compute_value(grid, goal, cost)
    for row in vals:
        print(row)
