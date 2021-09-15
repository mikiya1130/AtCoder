A = list(map(int, input().split()))

if 7 in A:
    A.remove(7)
    if set(A) == {5}:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
