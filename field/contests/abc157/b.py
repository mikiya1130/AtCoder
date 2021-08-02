a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
A = a1 + a2 + a3

N = int(input())

for i in range(N):
    b = int(input())
    if b in A:
        A[A.index(b)] = 0

lines = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

for line in lines:
    if A[line[0]] + A[line[1]] + A[line[2]] == 0:
        print("Yes")
        break
else:
    print("No")
