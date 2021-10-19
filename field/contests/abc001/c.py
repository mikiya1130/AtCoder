Deg, Dis = map(int, input().split())


def dir(Deg):
    if 112.5 <= Deg < 337.5:
        return "NNE"
    elif 337.5 <= Deg < 562.5:
        return "NE"
    elif 562.5 <= Deg < 787.5:
        return "ENE"
    elif 787.5 <= Deg < 1012.5:
        return "E"
    elif 1012.5 <= Deg < 1237.5:
        return "ESE"
    elif 1237.5 <= Deg < 1462.5:
        return "SE"
    elif 1462.5 <= Deg < 1687.5:
        return "SSE"
    elif 1687.5 <= Deg < 1912.5:
        return "S"
    elif 1912.5 <= Deg < 2137.5:
        return "SSW"
    elif 2137.5 <= Deg < 2362.5:
        return "SW"
    elif 2362.5 <= Deg < 2587.5:
        return "WSW"
    elif 2587.5 <= Deg < 2812.5:
        return "W"
    elif 2812.5 <= Deg < 3037.5:
        return "WNW"
    elif 3037.5 <= Deg < 3262.5:
        return "NW"
    elif 3262.5 <= Deg < 3487.5:
        return "NNW"
    else:
        return "N"


def w(Dis):
    Dis = Dis * 100 // 60
    if 0 <= Dis < 25:
        return 0
    elif 25 <= Dis < 155:
        return 1
    elif 155 <= Dis < 335:
        return 2
    elif 335 <= Dis < 545:
        return 3
    elif 545 <= Dis < 795:
        return 4
    elif 795 <= Dis < 1075:
        return 5
    elif 1075 <= Dis < 1385:
        return 6
    elif 1385 <= Dis < 1715:
        return 7
    elif 1715 <= Dis < 2075:
        return 8
    elif 2075 <= Dis < 2445:
        return 9
    elif 2445 <= Dis < 2845:
        return 10
    elif 2845 <= Dis < 3265:
        return 11
    else:
        return 12


Dir = dir(Deg)
W = w(Dis)
if W == 0:
    Dir = "C"

print(Dir, W)
