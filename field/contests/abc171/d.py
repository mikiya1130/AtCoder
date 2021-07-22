import collections

N = int(input())
A = list(map(int, input().split()))

countA = collections.Counter(A)
S = sum(A)

Q = int(input())

for i in range(Q):
    B, C = list(map(int, input().split()))

    if B in countA:
        S += (C - B) * countA[B]
        countA[C] += countA.pop(B)

    print(S)
