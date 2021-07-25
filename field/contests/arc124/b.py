N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = []
for b in B:
    X.append(A[0] ^ b)

ans = []
sortA = sorted(A)
for x in set(X):
    C = [b ^ x for b in B]

    sortC = sorted(C)
    for a, c in zip(sortA, sortC):
        if a != c:
            break
    else:
        ans.append(x)

print(len(ans))
for a in sorted(ans):
    print(a)
