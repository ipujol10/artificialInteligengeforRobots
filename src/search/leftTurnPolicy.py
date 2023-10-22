# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0],  # go up
           [0, -1],  # go left
           [1,  0],  # go down
           [0,  1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making
# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def isValidCell(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


def makePath(grid, init, goal, values):
    path = [[' ' for _ in row] for row in grid]
    x, y = goal
    path[x][y] = '*'
    print(values[x][y])

    return path


def optimum_policy2D(grid, init, goal, cost):
    x, y, d = init
    searching = [[0, x, y, d]]
    values = [[[[-1, -1] for _ in forward] for _ in row] for row in grid]
    values[x][y][d] = [0, len(action)]
    while (searching):
        nextUp = min(searching)
        searching.remove(nextUp)
        g, x, y, d = nextUp
        for i, act in enumerate(action):
            d2 = (d + act) % len(forward)
            dx, dy = forward[d2]
            x2 = x + dx
            y2 = y + dy
            if (isValidCell(grid, x2, y2)):
                g2 = g + cost[i]
                nG = values[x2][y2][d2][0]
                if (nG < 0 or g2 < nG):
                    searching.append([g2, x2, y2, d2])
                    values[x2][y2][d2] = [g2, i]

    return makePath(grid, init, goal, values)


if __name__ == "__main__":
    val = optimum_policy2D(grid, init, goal, cost)
    for row in val:
        print(row)
