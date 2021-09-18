L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    if L <= a <= H:
        print(0)
    elif a < L:
        print(L - a)
    else:
        print(-1)
