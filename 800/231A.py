n = int(input())

# Read and parse the questions
questions = [input().strip() for _ in range(n)]

# Initiliaze the variables
solvable_questions = 0

for question in questions:
    if sum(question) > 2:
        solvable_questions += 1

print("\n"+ solvable_questions)
