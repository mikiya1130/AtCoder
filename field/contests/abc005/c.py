T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for b in B:
    for a in A:
        if a <= b <= a + T:
            A.remove(a)
            break
    else:
        print("no")
        break
else:
    print("yes")
