# 最大部分列和
#
# mss([-1, -1, 1, 1, 1, -1, -1])
# -> 3 = sum(1, 1, 1)
#
# mss([8, -3, 65, -20, -45, 100, 8, -17, 4, -14])
# -> 113 = sum(8, -3, 65, -20, -45, 100, 8)
#
# mss([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
# -> 187 = sum(59, 26, -53, 58, 97)

def mss(X):
    max_sum = 0
    s = 0

    for x in X:
        s += x
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s

    return max_sum
