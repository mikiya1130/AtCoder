X, K, D = map(int, input().split())

X = abs(X)
if X - K * D >= 0:
    print(X - K * D)
else:
    q = X // D
    mod = X % D

    if (K - q) % 2 == 0:
        print(mod)
    else:
        print(D - mod)
