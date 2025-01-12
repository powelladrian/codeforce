# Read dimensions
n, m = map(int, input().split()) 

# Read the grid
grid = [input().strip() for _ in range(n)]

# Initalize a flag for validity

is_valid = True

# Loop through the rows
for i in range(n):
    # Check if the row is uniform
    if len(set(grid[i])) !=1: # If there is more than one unique element
        is_valid = False
        break
    
    # Check if the row matches the previos row
    if i > 0 and grid[i] == grid[i - 1]: # Compare with the previous row
        is_valid = False
        break

if is_valid:
    print("YES")
else:
    print("NO")