N = int(input())
A = list(map(int, input().split()))
n = len(set(A))

if n == N:
    print("YES")
else:
    print("NO")
