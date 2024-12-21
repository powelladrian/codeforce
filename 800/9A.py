"""
let max_roll = max(Y,W)
dot wins if her roll >= max_roll
the number of winning outcomes is 6 - max_roll + 1

probability of winning = winning outcomes / total outcomes
"""

import math

# Input values

Y, W = map(int, input().split())

# Calculate the maximum roll needed
max_roll = max(Y,W)

# Calculate the number of winning outcomes
winning_outcomes = 6 - max_roll + 1

# Total outcomes
total_outcomes = 6

# Simplify the fraction
gcd = math.gcd(winning_outcomes, total_outcomes)
numerator = winning_outcomes // gcd
denominator = total_outcomes // gcd

# Output the result
print(f"{numerator}/{denominator}")