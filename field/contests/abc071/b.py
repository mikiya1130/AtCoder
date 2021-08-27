S = list(input())

for c in range(97, 123):
    if chr(c) not in S:
        print(chr(c))
        break
else:
    print("None")
