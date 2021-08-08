N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i, p in enumerate(P, start=1):
    if i != p:
        cnt += 1

if cnt <= 2:
    print("YES")
else:
    print("NO")
