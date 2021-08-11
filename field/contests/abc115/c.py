N, K = map(int,input().split())
H = [int(input()) for _ in range(N)]

H.sort()
Diff = [None]*(N-K+1)
for i in range(N-K+1):
    Diff[i] = H[i+K-1] - H[i]

print(min(Diff))
