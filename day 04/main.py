inputfile = "input.txt"
passports = []

# Read and parse file
with open(inputfile) as f:
    passport = dict()

    for line in f:
        # Each passport is separated by a new line
        if line == '\n':
            passports.append(passport)
            passport = dict()

        # Credentials on the same line are separated by spaces
        creds = line.split()

        # Credential key/value pairs are separated by :
        for cred in creds:
            k, v = cred.split(':')
            passport[k] = v

    passports.append(passport)

#--------------------------#
# Part 1 - Required fields #
#--------------------------#

# All required fields
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Set default valid_count
valid_count = 0

# Check if all required fields are present
for passport in passports:
    if all([field in passport.keys() for field in required_fields]):
        valid_count += 1

print(valid_count)


#-----------------------#
# Part 2 - Valid fields #
#-----------------------#

# All required fields with their validation function
validation = [
    ('byr', lambda x: int(x) >= 1920 and int(x) <= 2002),
    ('iyr', lambda x: int(x) >= 2010 and int(x) <= 2020),
    ('eyr', lambda x: int(x) >= 2020 and int(x) <= 2030),
    ('hgt', lambda x: (int(x[:-2]) >= 150 and int(x[:-2]) <= 193 and x[-2:] == 'cm') or (int(x[:-2]) >= 59 and int(x[:-2]) <= 76 and x[-2:] == 'in')),
    ('hcl', lambda x: len(x[1:]) == 6 and x[0] == '#'),
    ('ecl', lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    ('pid', lambda x: len(x) == 9 and x.isdigit())
]

# Set default valid_count
valid_count = 0

# Go through all passports...
for passport in passports:
    is_valid = True
    # Go through all fields to be validated
    for field, val_func in validation:
        # If a field is not present, it's not valid
        if field not in passport.keys():
            is_valid = False
            break
        # If a field does not return True on the validation function, it's not valid
        if not val_func(passport[field]):
            is_valid = False
            break

    # Add to the valid_count if the passport is valid
    if is_valid:
        valid_count += 1

print(valid_count)
