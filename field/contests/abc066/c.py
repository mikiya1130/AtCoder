n = int(input())
A = list(map(int, input().split()))

oddB = A[::2]
evenB = A[1::2]

if len(A) % 2 == 0:
    B = list(reversed(evenB)) + oddB
else:
    B = list(reversed(oddB)) + evenB

print(*B)
