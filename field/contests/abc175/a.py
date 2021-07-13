S = input()

for i in range(3, 0, -1):
    R = "R" * i
    if R in S:
        print(i)
        break
else:
    print(0)
