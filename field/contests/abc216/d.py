from collections import defaultdict, deque

N, M = map(int, input().split())

outs = defaultdict(list)
ins = defaultdict(int)

for _ in range(M):
    k = int(input())
    A = list(map(int, input().split())) + [0]

    for i in range(k):
        outs[A[i + 1]].append(A[i])
        ins[A[i]] += 1

q = deque(v1 for v1 in range(len(ins)) if ins[v1] == 0)

ans = 0
while q:
    v1 = q.popleft()
    ans += 1
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

if ans - 1 == N:
    print("Yes")
else:
    print("No")
