import itertools

N = int(input())
A = list(map(int, input().split()))

end_0 = list(itertools.accumulate(A))

max_0 = [None] * N
max_0[0] = max(0, end_0[0])
for i in range(1, N):
    max_0[i] = max(max_0[i - 1], end_0[i])

end_ = [None] * N
max_ = [None] * N
end_[0] = end_0[0]
max_[0] = max_0[0]
for i in range(1, N):
    end_[i] = end_[i - 1] + end_0[i]
    max_[i] = max(max_[i - 1], end_[i - 1] + max_0[i])

print(max_[-1])
