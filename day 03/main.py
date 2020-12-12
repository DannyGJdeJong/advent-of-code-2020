import math

inputfile = "input.txt"
grid = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        line = line.replace('\n', '')
        grid.append(list(line) * 300)

# Get height of the grid
height = len(grid)

def tree_count_in_slope(x_step, y_step):
    # Set variables
    x = 0
    y = 0
    tree_count = 0

    # Keep looping until we hit the bottom
    while(y < height):
        # Check if we hit a tree
        if grid[y][x] == '#':
            tree_count += 1

        # Increase x and y by their steps
        x += x_step
        y += y_step

    return tree_count

#-----------------------#
# Part 1 - Single slope #
#-----------------------#

res = tree_count_in_slope(3, 1)
print("Part 1: {res}")


#----------------------------#
# Part 2 - Product of slopes #
#----------------------------#

# Define all slopes
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# Calculate tree_count per slope and take the product
res = math.prod([tree_count_in_slope(x_step, y_step) for x_step, y_step in slopes])
print("Part 2: {res}")
