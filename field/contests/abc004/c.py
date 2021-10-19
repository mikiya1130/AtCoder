N = int(input())

N %= 30
L = list(range(6))
for i in range(N):
    idx1 = i % 5
    idx2 = i % 5 + 1
    L[idx1], L[idx2] = L[idx2], L[idx1]

for l in L:
    print(l + 1, end="")
print()
