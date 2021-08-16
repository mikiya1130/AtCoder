A, B, C, X, Y = map(int, input().split())

if A + B <= 2 * C:
    print(A * X + B * Y)
else:
    ans = 2 * C * min(X, Y)
    if X > Y:
        if A <= 2 * C:
            ans += A * (X - Y)
        else:
            ans += 2 * C * (X - Y)
    else:
        if B <= 2 * C:
            ans += B * (Y - X)
        else:
            ans += 2 * C * (Y - X)
    print(ans)
