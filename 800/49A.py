# Read input
n = str(input())

# Manipulate string
n =  n.replace(" ","") # Remove whitespace
n = n[:-1] # Remove questionmark from the end
n = n.lower() # Convert to lowercase

# Retrieve last character
last_char = n[-1]

# Sets for vowels and consonants
vowels = {
    'a','e','i','o','u','y'
}
consonants = {
    'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'
}


if last_char in vowels:
    print("YES")
else:
    print("NO")

