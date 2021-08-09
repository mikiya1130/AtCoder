import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0] + list(itertools.accumulate(A))

ans = 0
j = 0
for i in range(N):
    while j < N + 1:
        if B[j] - B[i] >= K:
            ans += N - j + 1
            break
        j += 1

print(ans)
