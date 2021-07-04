A, B = map(int, input().split())

if A > B:
    print('No')
elif B / A <= 6:
    print('Yes')
else:
    print('No')
