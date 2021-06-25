N = int(input())
list = []
for i in range(N):
    A, B = map(int, input().split())
    list.append([A, B])

tmp1 = sorted(list, key=lambda x: x[0])
a1 = tmp1[0][0]
tmp1[0][1] += a1
tmp1.sort()
b1 = tmp1[0][1]

tmp2 = sorted(list, key=lambda x: x[1])
a2 = tmp2[0][1]
tmp2[0][0] += a2
tmp2.sort()
b2 = tmp2[0][0]

print(min(max(a1, b1), max(a2, b2)))
