N = int(input())

CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N):
    tmp = 0
    for c, s, f in CSF[i:]:
        if tmp <= s:
            tmp = s + c
        else:
            if tmp % f != 0:
                tmp += f - tmp % f
            tmp += c
    print(tmp)
