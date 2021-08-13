S = input()
K = int(input())

for i, s in enumerate(S):
    if s != "1":
        idx = i
        break
else:
    print(1)
    exit()

if K < idx + 1:
    print(1)
else:
    print(S[idx])
