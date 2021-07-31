S = input()

center = len(S) // 2

SL = S[:center]
SR = S[center + 1 :]

if SL == SR:
    sl_center = center // 2
    for i in range(sl_center):
        if SL[i] != SL[center - i - 1]:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
