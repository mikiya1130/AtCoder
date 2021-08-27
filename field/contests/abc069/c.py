N = int(input())
A = list(map(int, input().split()))

cnt = {0: 0, 2: 0, 4: 0}
for a in A:
    if a % 4 == 0:
        cnt[4] += 1
    elif a % 2 == 0:
        cnt[2] += 1
    else:
        cnt[0] += 1

if cnt[2] == 0:
    if cnt[0] - 1 <= cnt[4]:
        print("Yes")
    else:
        print("No")
else:
    if cnt[0] <= cnt[4]:
        print("Yes")
    else:
        print("No")
