# 백준 3552

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(X, Y, circles):
    total = 0
    for curX in range(X):
        # 현재 x가 curX일 때 각 원에 대해 흰색으로 칠해지는 y구간 저장
        line = []
        for cX, cY, cR in circles:
            if abs(cX - curX) <= cR:
                temp = (cR*cR - (cX-curX)*(cX-curX))**0.5
                line.append([max(0, math.ceil(cY-temp)), min(int(cY+temp), Y-1)])

        # 구간 병합 및 흰색 개수 도출
        if len(line) > 0:
            line.sort()
            prevS = line[0][0]
            prevE = line[0][1]
            for curS, curE in line:
                # 이전 구간과 겹치지 않는 경우
                if max(prevS, curS) > min(prevE, curE):
                    total += prevE - prevS + 1
                    prevS = curS
                    prevE = curE
                else:
                    prevS = min(prevS, curS)
                    prevE = max(prevE, curE)
            total += prevE - prevS + 1

    return X*Y - total


def main():
    X, Y, N = map(int, input().split())
    circles = []
    for _ in range(N):
        circles.append(list(map(int, input().split())))

    print(solve(X, Y, circles))


main()
