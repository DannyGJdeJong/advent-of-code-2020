inputfile = "input.txt"
instructions = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Get rid of trailing spaces and newlines
        line = line.strip()
        action = line[0]
        value = int(line[1:])

        instructions.append((action, value))


#----------------------------------#
# Part 1 - Find Manhattan distance #
#----------------------------------#

# Create an enum for easy direction encoding
from enum import IntEnum

class Direction(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3

# Encode starting position
facing = Direction.E
east = 0
north = 0

# Go through all instructions
for action, value in instructions:
    # If there's a rotating action
    if action in ['R', 'L']:
        # Go from degrees to number of quarter turns
        value /= 90

        # Turn right
        if action == 'R':
            facing = Direction((facing + value) % 4)

        # Turn left
        elif action == 'L':
            facing = Direction((facing - value) % 4)

    # Go forward in the given direction
    elif action == 'F':
        if facing == Direction.N:
            north += value
        elif facing == Direction.E:
            east += value
        elif facing == Direction.S:
            north -= value
        elif facing == Direction.W:
            east -= value

    # Go north
    elif action == 'N':
        north += value

    # Go east
    elif action == 'E':
        east += value

    # Go south
    elif action == 'S':
        north -= value

    # Go west
    elif action == 'W':
        east -= value

# Get the Manhattan distance of the final location
manhattan_distance = abs(north) + abs(east)

print(manhattan_distance)


#--------------------------------------------------------------#
# Part 2 - Find Manhattan distance from alternate instructions #
#--------------------------------------------------------------#

# Encode starting position
waypoint_east = 10
waypoint_north = 1
boat_east = 0
boat_north = 0

# Go through all instructions
for action, value in instructions:
    # If there's a rotating action
    if action in ['R', 'L']:
        # Go from degrees to number of quarter turns
        value /= 90

        # Rotate waypoint around the boat
        # Rotate right
        if action == 'R':
            for _ in range(int(value)):
                temp = waypoint_east
                waypoint_east = waypoint_north
                waypoint_north = -temp

        # Rotate right
        elif action == 'L':
            for _ in range(int(value)):
                temp = waypoint_east
                waypoint_east = -waypoint_north
                waypoint_north = temp

    # Move towards waypoint
    elif action == 'F':
        boat_east += value * waypoint_east
        boat_north += value * waypoint_north

    # Move waypoint north
    elif action == 'N':
        waypoint_north += value

    # Move waypoint east
    elif action == 'E':
        waypoint_east += value

    # Move waypoint south
    elif action == 'S':
        waypoint_north -= value

    # Move waypoint west
    elif action == 'W':
        waypoint_east -= value

# Get the Manhattan distance of the final location
manhattan_distance = abs(boat_north) + abs(boat_east)

print(manhattan_distance)
