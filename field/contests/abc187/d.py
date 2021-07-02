import operator

N = int(input())

list = []
for i in range(N):
    A, B = map(int, input().split())
    list.append((2*A+B, A, A+B))

list = sorted(list, reverse=True)

sumA = sum(l[1] for l in list)
sumAB = 0

ans = 0
for l in list:
    sumA -= l[1]
    sumAB += l[2]
    ans += 1
    if sumAB > sumA:
        break

print(ans)
