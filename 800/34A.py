# Read input
n = int(input()) # Number of soldiers

heights = list(map(int, input().split()))

# Initalize variables

min_diff = float('inf') # Minimum height difference
soldiers = (1, 2) # Default pair (1-based indices)


# Loop through neighbours
for i in range(n):
    # Find the neighbor (circular case)
    next_i = (i + 1) % n # Wrap-around using modulo
    
    # Calculate the height differenece
    diff = abs(heights[i] - heights[next_i])

    # Update if a smaller difference is found
    if diff < min_diff:
        min_diff = diff
        soldiers = (i + 1, next_i + 1) # Convert to 1-based indices


# Output the result
print(soldiers[0], soldiers[1])
