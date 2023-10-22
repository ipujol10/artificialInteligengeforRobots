# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

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
    return closed[x][y] == -1 and grid[x][y] == 0


def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    h = heuristic[init[0]][init[1]]
    searching = [[h, 0, init[0], init[1]]]
    closed = [[-1 for _ in col] for col in grid]
    closed[init[0]][init[1]] = len(delta)
    expand = [[-1 for _ in col] for col in grid]
    step = 0
    while (searching):
        nextUp = min(searching)
        searching.remove(nextUp)
        _, g, x, y = nextUp
        expand[x][y] = step
        if (isGoal(goal, x, y)):
            return expand
        for i, dlt in enumerate(delta):
            x2 = x + dlt[0]
            y2 = y + dlt[1]
            if (isValidCell(grid, closed, x2, y2)):
                g2 = g + cost
                h = heuristic[x2][y2]
                searching.append([h + g2, g2, x2, y2])
                closed[x2][y2] = i
        step += 1
    return "fail"


if __name__ == "__main__":
    expand = search(grid, init, goal, cost, heuristic)
    for col in expand:
        print(col)
