N, M = map(int, input().split())

maxL, minR = 1, N
for _ in range(M):
    L, R = map(int, input().split())
    maxL = max(maxL, L)
    minR = min(minR, R)

print(max(0, minR - maxL + 1))
