inputfile = "input.txt"
numbers = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Get rid of trailing spaces and newlines
        line = line.strip()
        number = int(line)

        # Append number
        numbers.append(number)


#----------------------------------#
# Part 1 - Find the invalid number #
#----------------------------------#

preamble_size = 25
invalid_number = 0

# Go through all numbers starting after the preamble
for i in range(preamble_size, len(numbers)):
    # Get number to analyse
    num = numbers[i]

    # Turn previous 25 nums into a set for quick lookup
    num_set = set(numbers[i-preamble_size:i])

    # Find if any combination of two numbers from the previous set of numbers
    # sum up to the current number
    previous_has_sum = any([num - n != n and num - n in num_set for n in num_set])

    # If no such combination can be found we found the invalid number
    if not previous_has_sum:
        invalid_number = num
        break

# Print the value
print(invalid_number)


#---------------------------------------#
# Part 2 - Find the encryption weakness #
#---------------------------------------#

# Start looking at the invalid number and work down
i = numbers.index(invalid_number) - 1

# Define encryption_weakness for when it's found
encryption_weakness = 0

# Loop until at the start of the list
while i >= 0:
    # Define variables
    sum_of_range = 0
    range_list = []

    # For n in i to 0
    for n in range(i, -1, -1):
        # Get current number and add it to range
        num = numbers[n]
        sum_of_range += num
        range_list.append(num)

        # Check if we found the correct sequence
        if sum_of_range >= invalid_number:
            if sum_of_range == invalid_number:
                # Stop looping
                i = 0
                encryption_weakness = min(range_list) + max(range_list)
            break

    # Decrease i by one so we go through the list backwards
    i -= 1

# Print the value
print(encryption_weakness)
