# Read input
borze_code = input()

# Prep for decoding
decoded = ''
i = 0

# Loop through the string
while i < len(borze_code):
    if borze_code[i] == '.':
        decoded += '0'
        i += 1
    elif borze_code[i] == "-":
        if borze_code[i + 1] == ".":
            decoded += '1'
        else:
            decoded += '2'
        i += 2

print(decoded)