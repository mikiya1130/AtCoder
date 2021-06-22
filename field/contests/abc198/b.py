import math

N = input()

L = len(N)
reverseN = [0] * L
for i in range(math.ceil(L/2)):
    reverseN[i] = N[L-i-1]
    reverseN[L-i-1] = N[i]

reverseN = ''.join(reverseN)
reverseN = str(int(reverseN))

if N.startswith(reverseN):
    print('Yes')
else:
    print('No')
