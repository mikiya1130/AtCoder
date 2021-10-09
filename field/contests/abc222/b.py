N, P = map(int, input().split())
A = list(map(int, input().split()))

B = [a for a in A if a < P]

print(len(B))
