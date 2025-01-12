# Read input
n, d = map(int, input().split())

heights = list(map(int, input().split()))

# Initialize counter
count = 0

for i in range(n):
    for j in range(n):
        if i != j and abs(heights[i] - heights[j]) <= d:
            count += 1
print(count)