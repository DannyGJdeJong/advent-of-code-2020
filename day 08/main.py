inputfile = "input.txt"
instructions = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Get rid of trailing spaces and newlines
        line = line.strip()

        # Split line into operation and argument
        operation, argument = line.split(' ')
        argument = int(argument)

        # Append instruction
        instructions.append((operation, argument))


# Runs program until it loops or terminates
# Returns accumulator value and whether it properly terminates
def run_instructions(instructions):
    accumulator = 0
    steps_taken = set()
    step = 0

    # Keep going through the program until we encounter a loop or the step exceeds the number of instructions
    while step not in steps_taken and step < len(instructions):
        # Add step to set so we don't end up in a loop
        steps_taken.add(step)

        operation, argument = instructions[step]

        # Perform acc operation
        if operation == "acc":
            step += 1
            accumulator += argument
            continue

        # Perform nop operation
        if operation == "nop":
            step += 1
            continue

        # Perform jmp operation
        if operation == "jmp":
            step += argument
            continue

    # Return true for terminates if step is exactly at exactly
    return (accumulator, step == len(instructions))


#----------------------------------------#
# Part 1 - Accumulator value before loop #
#----------------------------------------#

acc, terminates = run_instructions(instructions)
print(acc)


#----------------------------------------------#
# Part 2 - Fix program such that it terminates #
#----------------------------------------------#

# Loop through all instructions
for i in range(len(instructions)):
    operation, argument = instructions[i]

    # If operation is nop, switch it with jmp
    if operation == "nop":
        instructions_copy = instructions.copy()
        instructions_copy[i] = ("jmp", argument)

        # Run the program with adjusted instructions
        acc, terminates = run_instructions(instructions_copy)

        # If it terminates, print the accumulator
        if terminates:
            print(acc)
            break

        # Skip second if since we already handled this i
        continue

    # If operation is jmp, switch it with nop
    if operation == "jmp":
        instructions_copy = instructions.copy()
        instructions_copy[i] = ("nop", argument)

        # Run the program with adjusted instructions
        acc, terminates = run_instructions(instructions_copy)

        # If it terminates, print the accumulator
        if terminates:
            print(acc)
            break
