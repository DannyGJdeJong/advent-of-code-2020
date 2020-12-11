inputfile = "input.txt"
grid_orig = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Get rid of trailing spaces and newlines
        line = line.strip()
        line = list(line)

        # Append line
        grid_orig.append(line)


#--------------------------------#
# Part 1 - Short sighted seating #
#--------------------------------#

# Make a deep copy of the grid so it can be re-used later
import copy
grid = copy.deepcopy(grid_orig)

# Get the row and column counts
rows = len(grid)
cols = len(grid[0])

from itertools import product

def surrounded_occupied_count(grid, row_id, col_id):
    # Create offset list
    offsets = list(product([-1, 0, 1], [-1, 0, 1]))
    offsets.remove((0, 0))

    # Make a list of seats to check
    to_check = [(row + row_id, col + col_id) for row, col in offsets]
    to_check = [(row, col) for row, col in to_check if 0 <= row < rows and 0 <= col < rows]

    return sum([grid[row][col] == '#' for row, col in to_check])

# Keep looping until it breaks
while True:
    # Make a copy of the grid so changes don't ruin the loop
    grid_copy = copy.deepcopy(grid)

    # Go through all seats
    for row_id, row in enumerate(grid_copy):
        for col_id, col in enumerate(row):
            # Get the seat value
            seat = grid_copy[row_id][col_id]

            # If there's no seat, ignore it
            if seat == '.':
                continue

            # Count occupied seats directly surrounding the seat
            occ_count = surrounded_occupied_count(grid_copy, row_id, col_id)

            # If seat is empty and not surrounded by any chairs, mark it as occupied
            if seat == 'L' and occ_count == 0:
                grid[row_id][col_id] = '#'
                continue

            # If seat is occupied and surrounded by 4 or more other chairs, mark it empty
            if seat == '#' and occ_count >= 4:
                grid[row_id][col_id] = 'L'
                continue

    # If nothing changed, stop
    if grid == grid_copy:
        break

# Count the amount of occupied seats
occupied_seat_count = sum([row.count('#') for row in grid])

print(occupied_seat_count)


#------------------------------#
# Part 2 - Far sighted seating #
#------------------------------#

# Make a deep copy of the grid so it can be re-used later
import copy
grid = copy.deepcopy(grid_orig)

# Get the row and column counts
rows = len(grid)
cols = len(grid[0])

from itertools import product
from itertools import count

def far_sighted_occupied_count(grid, row_id, col_id):
    # Create directions list
    directions = list(product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0, 0))

    # Small lambda to check whether an offset is in range
    is_in_range = lambda row_offset, col_offset: 0 <= (row_id + row_offset) < rows and 0 <= (col_id + col_offset) < rows

    occupied_count = 0

    # Go through each direction
    for row, col in directions:
        # Check all seats with offset i in a certain direction
        for i in count(start=1):
            row_offset = row * i
            col_offset = col * i

            # If this chair is not in range, we've reached the edge without finding a seat
            if not is_in_range(row_offset, col_offset):
                break

            # Get the seat value
            seat = grid[row_id + row_offset][col_id + col_offset]

            # If no seat is present, check the next seat in this direction
            if seat == '.':
                continue

            # If an empty chair is present, stop checking in this direction
            if seat == 'L':
                break

            # If an occupied chair is present, stop checking in this direction and add one to the occupied count
            if seat == '#':
                occupied_count += 1
                break

    return occupied_count

# Keep looping until it breaks
while True:
    # Make a copy of the grid so changes don't ruin the loop
    grid_copy = copy.deepcopy(grid)

    # Go through all seats
    for row_id, row in enumerate(grid_copy):
        for col_id, col in enumerate(row):
            # Get the seat value
            seat = grid_copy[row_id][col_id]

            # If there's no seat, ignore it
            if seat == '.':
                continue

            # Count occupied seats surrounding the seat
            occ_count = far_sighted_occupied_count(grid_copy, row_id, col_id)

            # If seat is empty and not surrounded by any chairs, mark it as occupied
            if seat == 'L' and occ_count == 0:
                grid[row_id][col_id] = '#'
                continue

            # If seat is occupied and surrounded by 5 or more other chairs, mark it empty
            if seat == '#' and occ_count >= 5:
                grid[row_id][col_id] = 'L'
                continue

    # If nothing changed, stop
    if grid == grid_copy:
        break

# Count the amount of occupied seats
occupied_seat_count = sum([row.count('#') for row in grid])

print(occupied_seat_count)
