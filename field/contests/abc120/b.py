A, B, K = map(int,input().split())

n = 0
for i in range(100, 0, -1) :
    if A % i == 0 and B % i == 0:
        n += 1
        if n >= K:
            break

print(i)
