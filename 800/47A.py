import math

def is_triangle_number(n):
    # Step 1: Compute the discriminant
    discriminant = 1 + 8 * n

    # Step 2: Check if the discriminant is a perfect square
    sqrt_discriminant = int(math.sqrt(discriminant))
    if sqrt_discriminant * sqrt_discriminant != discriminant: 
        return False # Not a triangular number
    
    # Step 3: Calculate n
    k = (-1 + sqrt_discriminant) / 2 # Solve for k

    # Step 4: Check if n i s a positive integer
    return k.is_integer()

# Example usage
n = int(input())

if is_triangle_number(n):
    print("YES")
else: 
    print("NO")