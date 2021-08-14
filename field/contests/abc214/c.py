N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = [None] * N
tmp = None
start = T.index(min(T))
for i in range(N):
    idx = (start + i) % N
    if i == 0:
        ans[idx] = T[idx]
    else:
        ans[idx] = min(T[idx], tmp)
    tmp = ans[idx] + S[idx]

for a in ans:
    print(a)
