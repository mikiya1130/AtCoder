import bisect

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

time = [0]
l = [0]
for a, b in AB:
    time.append(time[-1] + a / b)
    l.append(l[-1] + a)

half = time[-1] / 2
n = bisect.bisect_right(time, half) - 1
rest = half - time[n]
cm = rest * AB[n][1]
ans = l[n] + cm

print(ans)
