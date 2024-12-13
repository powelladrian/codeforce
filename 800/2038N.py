#Input reading
t = int(input("")) # Reads the first line as an integer
test_cases = [input().strip() for _ in range(t)] # Reads and strips whitespace for each test case

#Operations directory for dynamic evaluation
operations = {
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '=': lambda a, b: a == b
}

#Function to check if expression evaluates to True
def is_valid(a, op, b):
    return operations[op](a, b)  # Dynamically evaluate the expression

# Function to fix invalid expressions
def fix_expression(a, op, b):
    if a < b:
        return f"{a}<{b}"
    elif a > b:
        return f"{a}>{b}"
    else:
        return f"{a}={b}"

fixed_test_cases = []
for expression in test_cases:
    for char in expression:
        if char not in '0123456789': # Store it as op
            op = char
            index_of_op = expression.index(op)
            a = int(expression[:index_of_op])
            b = int(expression[index_of_op + 1:])
            break
    
        # Check validity
    if is_valid(a, op, b):
        fixed_test_cases.append(expression)  # Append as-is if valid
    else:
        fixed_expression = fix_expression(a, op, b)  # Fix the invalid expression
        fixed_test_cases.append(fix_expression(a, op, b))  # Append fixed expression

# Print the fixed expressions in the same format as the input
for fixed_expression in fixed_test_cases:
    print(fixed_expression)