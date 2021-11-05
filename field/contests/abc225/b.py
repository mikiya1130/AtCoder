import collections

N = int(input())
AB = [list(map(int,input().split())) for _ in range(N-1)]

l = []
for ab in AB:
    l += ab
l = collections.Counter(l).values()
l = collections.Counter(l)

if l[1] == N-1:
    print("Yes")
else:
    print("No")
