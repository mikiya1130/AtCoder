# 最も近い要素のインデックスを返す
#
# - O(n)
# - 先頭インデックス優先
# - L = []のときNoneが返る
#
# get_nearest([1, 3, 5], 4)
# -> 1
#
# get_nearest([1, 5, 3], 4)
# -> 1
#
# get_nearest([1, 3, 3], 4)
# -> 1
#
def get_nearest_index(L, num):
    idx = None

    min_diff = None
    for i, l in enumerate(L):
        diff = abs(l - num)
        if min_diff is None or diff < min_diff:
            idx = i
            min_diff = diff

    return idx
