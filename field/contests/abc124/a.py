A, B = map(int, input().split())

L = [A, A - 1, B, B - 1]
L.sort(reverse=True)
print(sum(L[:2]))
