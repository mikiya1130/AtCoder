A, B, C = map(int, input().split())

ans = C
while ans <= B:
    if A <= ans:
        print(ans)
        break
    ans += C
else:
    print(-1)
