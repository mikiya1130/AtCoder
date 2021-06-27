N = int(input())

list = []
for i in range(N):
    A, P, X = map(int, input().split())
    if X - A > 0:
        list.append(P)

if len(list) == 0:
    ans = -1
else:
    ans = min(list)

print(ans)
