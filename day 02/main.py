inputfile = "input.txt"
passwords = []

# Read and parse file
with open(inputfile) as f:
    for line in f:
        # Split line into policy letter and password
        policy, letter, password = line.split()
        # Split 1-3 into 1 and 3
        mi, ma = policy.split('-')
        mi = int(mi)
        ma = int(ma)

        # Get just the letter instead of the : as well
        letter = letter[0]

        # Append to password list
        passwords.append((mi, ma, letter, password))

#-----------------------------#
# Part 1 - Min/max occurances #
#-----------------------------#

valid_count = 0

# Go through all passwords
for mi, ma, letter, password in passwords:
    # Get number of occurances
    count = password.count(letter)
    # If count is at least min and at most max it's a valid password
    if count >= mi and count <= ma:
        valid_count += 1

print(valid_count)

#------------------------------#
# Part 2 - Location occurances #
#------------------------------#

valid_count = 0

# Go through all passwords
for mi, ma, letter, password in passwords:
    # If letter occurs at min-th pos XOR at max-th pos it's a valid password
    if (password[mi - 1] == letter) ^ (password[ma - 1] == letter):
        valid_count += 1

print(valid_count)
