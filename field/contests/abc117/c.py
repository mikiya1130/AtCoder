N, M = map(int,input().split())
X = list(map(int,input().split()))

X.sort()

D = [None] * (M - 1)
for i in range(M-1):
    D[i] = X[i+1] - X[i]

D.sort()

if M-N > 0:
    print(sum(D[:M-N]))
else:
    print(0)
