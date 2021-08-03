import collections

N = int(input())

S = []
for i in range(N):
    s = input()
    S.append(s)

S = collections.Counter(S)
n = max(S.values())
ans = [k for k, v in S.items() if v == n]
ans = sorted(ans)

for a in ans:
    print(a)
