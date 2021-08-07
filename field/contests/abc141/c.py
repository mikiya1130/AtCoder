N, K, Q = map(int, input().split())

score = [K - Q] * N

for _ in range(Q):
    a = int(input())
    score[a - 1] += 1

for s in score:
    if s > 0:
        print("Yes")
    else:
        print("No")
