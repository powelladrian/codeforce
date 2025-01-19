# Read the input
n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())

total_years = sum(d[a-1 : b-1]) # Slicing the list from a-1 to b-1

# Output the result
print(total_years)