# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
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
    # modify code below
    # ----------------------------------------
    expand = [[-1 for _ in col] for col in grid]
    open = [[0, init[0], init[1]]]
    closed = [[0 for _ in col] for col in grid]
    closed[init[0]][init[1]] = 1
    step = 0
    while (open):
        next = min(open)
        open.remove(next)
        g, x, y = next
        expand[x][y] = step
        if (isGoal(goal, x, y)):
            break
        for dlt in delta:
            x2 = x + dlt[0]
            y2 = y + dlt[1]
            if (isValidCell(grid, closed, x2, y2)):
                open.append([g + cost, x2, y2])
                closed[x2][y2] = 1
        step += 1
    return expand


if __name__ == "__main__":
    expand = search(grid, init, goal, cost)
    for col in expand:
        print(col)
