S = input()

YYMM = False
MMYY = False
if 1 <= int(S[2:]) <= 12:
    YYMM = True
if 1 <= int(S[:2]) <= 12:
    MMYY = True

if YYMM and MMYY:
    print("AMBIGUOUS")
elif YYMM:
    print("YYMM")
elif MMYY:
    print("MMYY")
else:
    print("NA")
