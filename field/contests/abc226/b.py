N = int(input())
LA = [input() for _ in range(N)]

S = set()
for A in LA:
    A = A[1:]
    S.add(A)

print(len(S))
