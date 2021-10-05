A, B, C = map(int, input().split())

if A + B == C:
    plus = True
else:
    plus = False

if A - B == C:
    minus = True
else:
    minus = False

if plus and minus:
    print("?")
elif plus:
    print("+")
elif minus:
    print("-")
else:
    print("!")
