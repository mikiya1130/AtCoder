n, m = map(int, input().split())

deg_n = 360 * (n % 12) // 12 + 30 * m / 60
deg_m = 360 * m // 60

deg = abs(deg_n - deg_m)
deg = min(deg, 360 - deg)

print(deg)
