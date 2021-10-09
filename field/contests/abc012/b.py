N = int(input())

hh, N = divmod(N, 3600)
mm, dd = divmod(N, 60)

print("{:02d}:{:02d}:{:02d}".format(hh, mm, dd))
