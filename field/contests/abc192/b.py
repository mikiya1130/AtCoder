S = list(input())

odd = S[::2]
even = S[1::2]

odd = ''.join(odd)
even = ''.join(even)

if odd.islower() and (not even or even.isupper()):
    print('Yes')
else:
    print('No')
