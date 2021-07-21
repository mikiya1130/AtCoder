import collections

N = int(input())
C = input()

n_r = collections.Counter(C)["R"]
print(collections.Counter(C[:n_r])["W"])
