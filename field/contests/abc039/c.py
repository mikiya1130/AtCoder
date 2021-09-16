S = input()

A = [0 if s == "W" else 1 for s in S]
B = [A[i] + A[i + 1] for i in range(19)]
C = [i for i, b in enumerate(B) if b == 0]

if {4, 11} <= set(C):
    print("Do")
elif {2, 9} <= set(C):
    print("Re")
elif {0, 7} <= set(C):
    print("Mi")
elif {6, 11} <= set(C):
    print("Fa")
elif {4, 9} <= set(C):
    print("So")
elif {2, 7} <= set(C):
    print("La")
elif {0, 5} <= set(C):
    print("Si")
