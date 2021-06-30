N = int(input())
A = list(map(int, input().split()))

first = A.index(max(A))

center = 2 ** (N-1)
if first >= center:
    B = A[:center]
else:
    B = A[center:]

second = A.index(max(B))
print(second+1)
