N = int(input())
P = [int(input()) for _ in range(N)]

P.sort()
P[-1] //= 2

print(sum(P))
