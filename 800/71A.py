# if len > 10 word is considered too long and should be replaced wiht an abbreviation
# the abbreviation will be the first and last letter and in between the number of letters between the first and last letter
# process should be automated and the output should be the abbreciated too long words and the short words in the same format

n = int(input())

# Read and parse the words into a list
words = [input().strip() for _ in range(n)]

# Final list of words
results = []

for word in words:
    if len(word) > 10:
        #add logic for changing word so that it is the first and last letter and num of letters inbetween
        word_len = (len(word) - 2)
        word  = word[0] + str(word_len) + word[-1]
        results.append(word.lower())
    else:
        results.append(word.lower())

print("\n".join(results)) # Print all results