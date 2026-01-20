# 백준 4140

import io
from math import sqrt

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
r = 2.5
EPS = 1e-9


def solve(N, points):
    maxCount = 1
    for i in range(N-1):
        for j in range(i+1, N):
            # i번 점, j번 점이 원주 위에 있도록 원의 중심 좌표 구하기
            dx = points[j][0]-points[i][0]
            dy = points[j][1]-points[i][1]
            d2 = dx*dx + dy*dy
            if d2 > 4*r*r + EPS:
                continue
            d = sqrt(d2)
            mX = (points[i][0] + points[j][0]) / 2
            mY = (points[i][1] + points[j][1]) / 2
            h = sqrt(max(0, r*r - d2/4))

            circle = [(mX - dy*h/d, mY + dx*h/d), (mX + dy*h/d, mY - dx*h/d)]

            # (cX, cY)가 중심 좌표일 때, 해당 원 내부에 존재하는 점의 개수 체크
            for cX, cY in circle:
                count = 0
                for k in range(N):
                    if (points[k][0]-cX)**2 + (points[k][1]-cY)**2 <= r*r + EPS:
                        count += 1

                maxCount = max(maxCount, count)

    return maxCount


def main():
    N = 0
    points = []
    while True:
        try:
            a, b = map(float, input().split())
            points.append((a, b))
            N += 1
        except Exception:
            break
    print(solve(N, points))


main()
