N = int(input())

yen = 0
btc = 0
for _ in range(N):
    x, u = input().split()
    if u == 'JPY':
        yen += int(x)
    elif u == 'BTC':
        btc += float(x)

print(yen + btc * 380000)
