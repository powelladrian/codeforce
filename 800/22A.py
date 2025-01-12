# Input number of numbers
n = int(input())

# Read and parse the numbers
nums = list(map(int, input().split()))

# Remove duplicates and sort
distinct_nums = sorted((set(nums)))

# Check if there is a second smallest number
if len(distinct_nums) <= 1:
    print("NO")
else:
    print(distinct_nums[1]) # Second smallest number
