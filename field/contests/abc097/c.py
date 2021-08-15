s = input()
K = int(input())

l = len(s)
S = []
for i in range(l):
    for w in range(1, 6):
        if i + w <= l:
            S.append(s[i : i + w])

print(sorted(set(S))[K - 1])
