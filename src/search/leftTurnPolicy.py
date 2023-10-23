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
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return False
    return grid[x][y] == 0


def getPath(policy, init):
    x, y, o = init
    policy2D = [[' ' for _ in row] for row in policy]
    policy2D[x][y] = policy[x][y][o]
    while (policy[x][y][o] != '*'):
        match policy[x][y][o]:
            case 'R':
                o2 = (o - 1) % 4
            case 'L':
                o2 = (o + 1) % 4
            case '#':
                o2 = o
            case _:
                raise ValueError
        x += forward[o2][0]
        y += forward[o2][1]
        o = o2
        policy2D[x][y] = policy[x][y][o]

    return policy2D


def optimum_policy2D(grid, init, goal, cost):
    x, y = goal
    searching = [[0, x, y, i] for i in range(len(forward))]
    value = [[[999 for _ in forward] for _ in row] for row in grid]
    policy = [[[' ' for _ in forward] for _ in row] for row in grid]
    for i in range(len(forward)):
        policy[x][y][i] = '*'
    while (searching):
        nextUp = min(searching)
        searching.remove(nextUp)
        g, x, y, o = nextUp
        value[x][y][o] = g
        for act, char, cst in zip(action, action_name, cost):
            o2 = (o - act) % len(forward)
            dx, dy = forward[o]
            x2 = x - dx
            y2 = y - dy
            if (isValidCell(grid, x2, y2)):
                v2 = g + cst
                if (v2 < value[x2][y2][o2]):
                    searching.append([v2, x2, y2, o2])
                    policy[x2][y2][o2] = char

    return getPath(policy, init)


if __name__ == "__main__":
    val = optimum_policy2D(grid, init, goal, cost)
    for row in val:
        print(row)
