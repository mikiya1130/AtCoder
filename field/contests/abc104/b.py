S = input()

c = -1
if "C" in S:
    c = S.index("C")

if S[0] == "A" and 2 <= c <= len(S) - 2 and S[1:c].islower() and S[c + 1 :].islower():
    print("AC")
else:
    print("WA")
