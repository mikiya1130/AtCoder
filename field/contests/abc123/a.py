A = [int(input()) for _ in range(5)]
k = int(input())

if A[4] - A[0] <= k:
    print('Yay!')
else:
    print(':(')
