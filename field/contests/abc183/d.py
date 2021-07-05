import itertools

N, W = map(int, input().split())

l = [0] * (2 * 10 ** 5 + 1)

for _ in range(N):
    S, T, P = map(int, input().split())
    l[S] += P
    l[T] -= P

for w in itertools.accumulate(l):
    if w > W:
        print("No")
        break
else:
    print("Yes")
