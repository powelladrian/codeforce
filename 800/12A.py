def is_symmetric(keypad_matrix):
    # Define the pairs of indices to compare
    pairs = [
        ((0,0),(2,2)),
        ((0,1),(2,1)),
        ((0,2),(2,0)),
        ((1,0),(1,2))
    ]

    # Loop through each pair and compare
    for (x1, y1), (x2, y2) in pairs:
        if keypad_matrix[x1][y1] != keypad_matrix[x2][y2]:
            return "NO"
    return "YES"

keypad_matrix = [list(input().strip()) for _ in range(3)]

print(is_symmetric(keypad_matrix))