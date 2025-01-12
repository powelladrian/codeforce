# Read dimensions
n, m = map(int, input().split()) 

# Read the grid
grid = [input().strip() for _ in range(n)]

# Initalize the boundaries
top_boundary = float('inf')
bottom_boundary = 0
left_boundary = float('inf')
right_boundary = 0

# Find the boundaries
for i in range(n): # Loop through rows
    for j in range(m): # Loop through columns
        if grid[i][j] == '*': # Check for a shaded square
            # Update boundaries
            top_boundary = min(top_boundary, i)
            bottom_boundary = max(bottom_boundary, i)
            left_boundary = min(left_boundary, j)
            right_boundary = max(right_boundary, j)
# Extract the rectangle
for i in range(top_boundary, bottom_boundary + 1): # Rows in the rectangle
    print(grid[i][left_boundary:right_boundary + 1]) # Columns in the rectangle

