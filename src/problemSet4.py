# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------


def isValidCell(grid, x, y):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return False
    return grid[x][y] == 0


def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    # Probability(stepping left) = prob(stepping right) = failure_prob
    failure_prob = (1.0 - success_prob)/2.0
    x, y = goal
    value = [[collision_cost for _ in row] for row in grid]
    value[x][y] = 0
    policy = [[' ' for _ in row] for row in grid]
    policy[x][y] = '*'
    changed = True
    while (changed):
        changed = False
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if (isValidCell(grid, x, y)):
                    for i, char in enumerate(delta_name):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if (isValidCell(grid, x2, y2)):
                            v2 = success_prob * value[x2][y2] + cost_step
                            for n in [-1, 1]:
                                i2 = (i + n) % 4
                                x2 = x + delta[i2][0]
                                y2 = y + delta[i2][1]
                                if (isValidCell(grid, x2, y2)):
                                    v2 += failure_prob * value[x2][y2]
                                else:
                                    v2 += failure_prob * collision_cost
                            if (v2 < value[x][y]):
                                value[x][y] = v2
                                policy[x][y] = char
                                changed = True

    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------


grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1]  # Goal is in top right corner
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value, policy = stochastic_value(
    grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print(row)
for row in policy:
    print(row)

# Expected outputs:
#
# [471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
# [334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977],
# [398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738],
# [700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
