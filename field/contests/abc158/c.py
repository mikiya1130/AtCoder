A, B = map(int, input().split())

for yen in range(1, 1010):
    if yen * 8 // 100 == A and yen // 10 == B:
        print(yen)
        break
else:
    print(-1)
