# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
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
    return closed[x][y] == -1 and grid[x][y] == 0


def getPrevious(current, step):
    x, y = current
    dx, dy = delta[step]
    return [x - dx, y - dy]


def makePath(grid, init, goal, closed):
    path = [[' ' for _ in col] for col in grid]
    path[goal[0]][goal[1]] = '*'
    current = goal
    while (current != init):
        step = closed[current[0]][current[1]]
        previous = getPrevious(current, step)
        path[previous[0]][previous[1]] = delta_name[step]
        current = previous
        previous = closed[current[0]][current[1]]
    return path


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    searching = [[0, init[0], init[1]]]
    closed = [[-1 for _ in col] for col in grid]
    closed[init[0]][init[1]] = len(delta)
    while searching:
        nextUp = min(searching)
        searching.remove(nextUp)
        g, x, y = nextUp
        if (isGoal(goal, x, y)):
            break
        for i, dlt in enumerate(delta):
            x2 = x + dlt[0]
            y2 = y + dlt[1]
            if (isValidCell(grid, closed, x2, y2)):
                searching.append([g + cost, x2, y2])
                closed[x2][y2] = i
    return makePath(grid, init, goal, closed)


if __name__ == "__main__":
    expand = search(grid, init, goal, cost)
    for col in expand:
        print(col)
