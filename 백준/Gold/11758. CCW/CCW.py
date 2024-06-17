# 백준 11758

import sys

input = sys.stdin.readline


# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    temp = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


def main():
    point = []
    for i in range(3):
        point.append(list(map(int, input().split())))
    
    print(CCW(point[0], point[1], point[2]))


main()