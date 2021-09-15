N = int(input())
A = list(map(int, input().split()))

A = [(i, a) for i, a in enumerate(A, start=1)]
A.sort(key=lambda x: x[1], reverse=True)

for i, _ in A[:N]:
    print(i)
