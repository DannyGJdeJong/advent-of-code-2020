inputfile = "input.txt"
rules_dict = dict()

# Read and parse file
with open(inputfile) as f:
    for line in f:
        rule_dict = dict()

        # Remove all instances of bags or bag
        # so that we can easily filter by just their names
        line = line.replace('bags', '')
        line = line.replace('bag', '')

        # Split the bag from its rules
        bag, rules = line.split('contain')
        bag = bag.strip()

        # If a bag contains no other bags, handle it differently
        if rules == " no other .\n":
            rule_dict[''] = 1
            rules_dict[bag] = rule_dict
            continue

        # Clean the rules
        rules = rules.replace('.', '')
        rules_list = rules.split(',')

        # Add all rules to a dict
        for rule in rules_list:
            rule = rule.strip()
            num, name = rule.split(' ', 1)
            rule_dict[name.strip()] = int(num)

        # Then finally add the rule_dict to the rules_dict
        rules_dict[bag] = rule_dict


#----------------------------------------------------#
# Part 1 - Count of bags that can hold the shiny bag #
#----------------------------------------------------#

bags_that_hold_shiny_bag = set()
length = -1

# Get started with all bags that can hold the shiny gold one directly
for bag, rules in rules_dict.items():
    if "shiny gold" in rules.keys():
        bags_that_hold_shiny_bag.add(bag)

# Then keep going until the length doesn't change
while length != len(bags_that_hold_shiny_bag):
    length = len(bags_that_hold_shiny_bag)

    # Make a copy so the set doesn't change while looping through it
    bags_that_hold_shiny_bag_copy = bags_that_hold_shiny_bag.copy()

    # Loop through the bags to search which bags can hold that one
    for bag_to_search in bags_that_hold_shiny_bag_copy:
        for bag, rules in rules_dict.items():
            if bag_to_search in rules.keys():
                bags_that_hold_shiny_bag.add(bag)

# Print the answer
print(len(bags_that_hold_shiny_bag))


#--------------------------------------------------#
# Part 2 - Count of bags that fit in the shiny bag #
#--------------------------------------------------#

bags_to_check = [("shiny gold", 1)]
total = -1

while len(bags_to_check) > 0:
    # Pop a bag from the bags to check list
    bag, num = bags_to_check.pop()
    rules = rules_dict[bag]

    # Add the number of bags to the total
    total = total + num

    # If no bags fit in this bag, continue
    if '' in rules.keys():
        continue

    # Add remaining bags and counts to the list to check
    bags_to_check.extend([(k, num * v) for k, v in rules.items()])

# Print the answer
print(total)
