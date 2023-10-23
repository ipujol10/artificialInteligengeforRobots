# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
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


def optimum_policy(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    x, y = goal
    searching = [[0, x, y]]
    value = [[99 for _ in row] for row in grid]
    policy = [[' ' for _ in row] for row in grid]
    policy[x][y] = '*'
    while (searching):
        nextUP = min(searching)
        searching.remove(nextUP)
        g, x, y = nextUP
        value[x][y] = g
        for dlt, char in zip(delta, delta_name):
            x2 = x - dlt[0]
            y2 = y - dlt[1]
            if (isValidCell(grid, x2, y2)):
                v2 = g + cost
                if (v2 < value[x2][y2]):
                    searching.append([g + cost, x2, y2])
                    policy[x2][y2] = char
    return policy


if (__name__ == "__main__"):
    vals = optimum_policy(grid, goal, cost)
    for row in vals:
        print(row)
