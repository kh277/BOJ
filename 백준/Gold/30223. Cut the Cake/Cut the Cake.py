# 백준 30223

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**6


def ShoelaceFormula(poly):
    area = 0

    for i in range(-1, len(poly)-1):
        j = i+1
        area += poly[i][0] * poly[j][1] - poly[i][1] * poly[j][0]
    
    return abs(area)/2


def solve(N, hull):
    result = INF
    for i in range(N-1):
        for j in range(i+1, N):
            if abs(i-j) < 2:
                continue
            result = min(result, abs(ShoelaceFormula(hull[0:i+1] + hull[j:N])-ShoelaceFormula(hull[i:j+1])))

    return round(result, 1)


def main():
    N = int(input())
    hull = []
    for _ in range(N):
        hull.append(tuple(map(int, input().split())))

    print(solve(N, hull))


main()
