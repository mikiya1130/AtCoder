import collections

n = int(input())
V = list(map(int, input().split()))

odd = V[::2]
even = V[1::2]

odd = collections.Counter(odd)
even = collections.Counter(even)

odd = sorted(odd.items(), reverse=True, key=lambda x: x[1])
even = sorted(even.items(), reverse=True, key=lambda x: x[1])

odd.append((0, 0))
even.append((0, 0))

if odd[0][0] == even[0][0]:
    if odd[0][1] + even[1][1] > odd[1][1] + even[0][1]:
        even[0], even[1] = even[1], even[0]
    else:
        odd[0], odd[1] = odd[1], odd[0]

ans = 0
for _, i in odd[1:]:
    ans += i
for _, i in even[1:]:
    ans += i
print(ans)
