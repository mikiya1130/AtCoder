N, M = map(int, input().split())

ac = [False] * N
wa = [0] * N

for _ in range(M):
    p, S = input().split()
    p = int(p) - 1

    if S == "AC":
        if ac[p] == False:
            ac[p] = True
    elif S == "WA":
        if ac[p] == False:
            wa[p] += 1

sum_ac = sum(ac)
sum_wa = 0
for _ac, _wa in zip(ac, wa):
    if _ac:
        sum_wa += _wa

print(sum_ac, sum_wa)
