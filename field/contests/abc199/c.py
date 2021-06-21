N = int(input())
S = input()
Q = int(input())

S1, S2 = [i for i in S[:N]], [i for i in S[N:]]

for _ in range(Q):
    T, A, B = map(int, input().split())

    if T == 1:
        if A-1 < N:
            if B-1 < N:
                S1[A-1], S1[B-1] = S1[B-1], S1[A-1]
            else:
                S1[A-1], S2[B-1-N] = S2[B-1-N], S1[A-1]
        else:
            if B-1 < N:
                S2[A-1-N], S1[B-1] = S1[B-1], S2[A-1-N]
            else:
                S2[A-1-N], S2[B-1-N] = S2[B-1-N], S2[A-1-N]
    else:
        S1, S2 = S2, S1

print(''.join(S1 + S2))
