inputfile = "input.txt"
boarding_passes = []

# Read and parse file
with open(inputfile) as f:
    # Append all passes to file
    for line in f:
        boarding_passes.append(line)

def decode_pass(boarding_pass, rows, columns):
    # Return seat ID when done
    if len(boarding_pass) == 0:
        return rows[0] * 8 + columns[0]

    # Get first character of boarding pass
    sign = boarding_pass[0]
    if sign in ['F', 'B']:
        # Take first half if F, else take second half
        new_rows = rows[:int(len(rows) / 2)] if sign == 'F' else rows[int(len(rows) / 2):]
        return decode_pass(boarding_pass[1:], new_rows, columns)
    else:
        # Take first half if L, else take second half
        new_columns = columns[:int(len(columns) / 2)] if sign == 'L' else columns[int(len(columns) / 2):]
        return decode_pass(boarding_pass[1:], rows, new_columns)

# Transform all boarding passes into seat_ids
seat_ids = [decode_pass(boarding_pass, range(128), range(8)) for boarding_pass in boarding_passes]


#----------------------#
# Part 1 - Max seat_id #
#----------------------#

# Get max seat id
max_seat_id = max(seat_ids)
print(max_seat_id)


#-----------------------#
# Part 2 - Find my seat #
#-----------------------#

# Transform seat_ids into a set for faster lookups
seat_ids_set = set(seat_ids)

# Find my own seat which has both its neighbouring seats in the plane
for i in range(max_seat_id):
    if i not in seat_ids_set and i + 1 in seat_ids_set and i - 1 in seat_ids_set:
        print(i)
