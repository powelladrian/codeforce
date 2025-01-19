# read input
n = int(input())

# init variables
current_child = 1 # ball always starts with child #1
result = [] # init as empty list
                # will store children who get the ball after each turn

# simulate the throws
for i in range(1, n): # there are n-1 throws
    # calculate the next child who gets the ball
    # current_child + i - 1) determines the 0-based index of the next child in the sequence
    # % n ensures the index wraps around if it exceeds the last child (circular structure)
    # + 1 converts the 0-based index back to 1-based (since the children are numbered from 1 to n)
    next_child = (current_child + i - 1) % n + 1

    # add this child to the result list (they recieve the ball after this throw)
    result.append(next_child)

    # update current_child to the child who just received the ball
    # this ensures the next throw starts from this child
    current_child = next_child

# output the result
# convert the list of integers (children's numbers) into a space-separated string
# map(str, result) converts each int in the result list to a string
# " ".join(...) combines them into a single string separated by spaces
print(" ".join(map(str, result)))
