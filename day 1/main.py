inputfile = "input.txt"
nums = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        nums.append(int(line))

# Sort nums
nums = sorted(nums)


#---------------------------------------------------#
# Part 1 - Find any two numbers that add up to 2020 #
#---------------------------------------------------#

# Go through all number combinations
for num in nums:
    for num_2 in nums:
        num_sum = num + num_2

        # Since numbers are sorted, don't try the next couple of combinations
        if num_sum > 2020:
            break

        if num_sum == 2020:
            print(num * num_2)
            break

#-----------------------------------------------------#
# Part 2 - Find any three numbers that add up to 2020 #
#-----------------------------------------------------#

# Go through all number combinations
for num in nums:
    for num_2 in nums:
        num_sum = num + num_2

        # Since numbers are sorted, don't try the next couple of combinations
        if num_sum > 2020:
            break

        for num_3 in nums:
            num_sum = num + num_2 + num_3

            # Since numbers are sorted, don't try the next couple of combinations
            if num_sum > 2020:
                break

            if num_sum == 2020:
                print(num * num_2 * num_3)
                break
