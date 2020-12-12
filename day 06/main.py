inputfile = "input.txt"
groups = []

# Read and parse file
with open(inputfile) as f:
    answers = []

    for line in f:
        # Each group is separated by a new line
        if line == '\n':
            groups.append(answers)
            answers = []
            continue

        # Add all answers as a list
        line = line.replace('\n', '')
        answers.append(list(line))

    # Add final set of answers
    groups.append(answers)


#----------------------------------#
# Part 1 - Count of unique answers #
#----------------------------------#

# Flatten the inner list of answers
flattened = [[letter for answer in group for letter in answer] for group in groups]

# Get the length of the set, since each answer only occurs once in each set
answer_count = sum([len(set(group)) for group in flattened])

print(answer_count)


#----------------------------------#
# Part 2 - Count of shared answers #
#----------------------------------#

# Turn all sets of answers into sets
group_sets = [[set(answers) for answers in group] for group in groups]

# Take the intersection of all of the groups' answers
intersections = [group[0].intersection(*group) for group in group_sets]

# Get the length of each of the intersections and sum them
answer_count = sum([len(group) for group in intersections])

print(answer_count)
