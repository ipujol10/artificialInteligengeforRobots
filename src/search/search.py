# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def isGoal(goal, x, y):
    return goal[0] == x and goal[1] == y


def isValidCell(grid, closed, x, y):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return False
    return closed[x][y] == 0 and grid[x][y] == 0


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    open = [[0, init[0], init[1]]]
    closed = [[0 for _ in col] for col in grid]
    closed[init[0]][init[1]] = 1
    while (open):
        next = min(open)
        open.remove(next)
        g, x, y = next
        if (isGoal(goal, x, y)):
            return next
        for dlt in delta:
            x2 = x + dlt[0]
            y2 = y + dlt[1]
            if (isValidCell(grid, closed, x2, y2)):
                open.append([g + cost, x2, y2])
                closed[x2][y2] = 1
    return "fail"


if __name__ == "__main__":
    print(search(grid, init, goal, cost))
