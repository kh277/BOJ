# 백준 29727

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(xa, ya, xb, yb):
    # 전체 경우의 수 n+1C2 * n+1C2
    result = (N+1)*(N+1)*N*N//4

    if xa > xb:
        xa, xb = xb, xa
    if ya > yb:
        ya, yb = yb, ya

    # 추가된 선분이 좌표축에 평행하지 않은 경우
    if xa != xb and ya != yb:
        return result

    # 추가된 선분이 x축에 평행한 경우
    elif xa != xb and ya == yb:
        # 추가된 선분이 범위 내에 존재하지 않는 경우
        if xb <= 0 or xa >= N-1:
            return result
        countX = math.floor(min(xb+0.5, N)) - math.ceil(max(xa+0.5, 0)) + 1
        temp = countX*(countX-1)//2 * (N+1)
        return result + temp

    # 추가된 선분이 y축에 평행한 경우
    else:
        # 추가된 선분이 범위 내에 존재하지 않는 경우
        if yb <= 0 or ya >= N-1:
            return result
        countY = math.floor(min(yb+0.5, N)) - math.ceil(max(ya+0.5, 0)) + 1
        temp = countY*(countY-1)//2 * (N+1)
        return result + temp


# main 함수 ----------
N = int(input())
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

print(solve(xa, ya, xb, yb))