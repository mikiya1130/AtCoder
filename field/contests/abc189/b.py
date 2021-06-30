N, X = map(int, input().split())

alcohol = 0
for n in range(N):
    V, P = map(int, input().split())
    alcohol += V * P

    if alcohol > X * 100:
        print(n + 1)
        break
else:
    print(-1)
