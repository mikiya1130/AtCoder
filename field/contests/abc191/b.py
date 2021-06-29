_, X = map(int, input().split())
A = list(map(int, input().split()))

ans = [i for i in A if i != X]

print(*ans)
