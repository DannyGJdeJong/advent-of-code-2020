inputfile = "input.txt"
adapters = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Get rid of trailing spaces and newlines
        line = line.strip()
        joltage = int(line)

        # Append number
        adapters.append(joltage)


#--------------------------------#
# Part 1 - Find jolt differences #
#--------------------------------#

# Built in adapter is 3 higher than max adapter
adapters.append(max(adapters) + 3)

# Sort adapters and reverse them
_adapters = sorted(adapters)
_adapters.reverse()

# Set some variables
previous_adapter = 0
diff_1_count = 0
diff_3_count = 0

# Go through all adapters
while len(_adapters) > 0:
    # Get lowest adapter
    adapter = _adapters.pop()
    diff = adapter - previous_adapter
    previous_adapter = adapter

    if diff == 1:
        diff_1_count += 1
        continue

    if diff == 3:
        diff_3_count += 1

# Output the amount of diff_1 times the amount of diff_3
print(diff_1_count * diff_3_count)


#-----------------------------------------------#
# Part 2 - Find number of distinct combinations #
#-----------------------------------------------#

# Built in adapter is 3 higher than max adapter
adapters.append(max(adapters) + 3)

# Sort adapters and reverse them
_adapters = sorted(adapters)
_adapters.reverse()

previous_adapter = 0

groups = []
current_group_size = 0

# Go through all adapters
while len(_adapters) > 0:
    # Get lowest adapter
    adapter = _adapters.pop()
    diff = adapter - previous_adapter
    previous_adapter = adapter

    if diff == 1:
        current_group_size += 1
        continue

    if diff == 3:
        groups.append(current_group_size)
        current_group_size = 0

# Group size vs amount of possibilities seems to follow a tribonacci sequence
# Only goes up to 4 since no groups are larger than 4
tribonacci = dict({
    0: 1,
    1: 1,
    2: 2,
    3: 4,
    4: 7
})

from math import prod

# Take the product of all numbers of possibilities
possibilities_count = prod([tribonacci[n] for n in groups])

print(possibilities_count)
