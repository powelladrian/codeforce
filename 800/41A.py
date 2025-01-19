word = input()
rword = input()

if word == rword[::-1]:
    print("YES")
else:
    print("NO")