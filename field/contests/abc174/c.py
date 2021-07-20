K = int(input())

a = 0
for i in range(1, K + 1):
    a = (10 * a + 7) % K
    if a == 0:
        print(i)
        break
else:
    print(-1)
