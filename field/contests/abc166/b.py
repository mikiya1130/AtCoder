N, K = map(int, input().split())

M = set()
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    M |= set(A)

print(N - len(M))
