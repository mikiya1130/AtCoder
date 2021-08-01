from collections import deque

S = deque(input())
Q = int(input())

reverse = False

for _ in range(Q):
    q = list(input().split())

    if q[0] == "1":
        reverse ^= True
    elif q[0] == "2":
        if (not reverse and q[1] == "1") or (reverse and q[1] == "2"):
            S.appendleft(q[2])
        else:
            S.append(q[2])

S = "".join(S)
if reverse:
    S = S[::-1]

print(S)
