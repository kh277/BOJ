# 백준 3097

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


# banList에 포함된 선분은 제외하고 이동했을 때, 최종 위치 반환
def getLastP(N, lines, banList):
    curX = 0
    curY = 0

    for i in range(N):
        if i not in banList:
            curX += lines[i][0]
            curY += lines[i][1]
    
    return [curX, curY]


# (0, 0) ~ (A, B)까지의 거리 반환
def getDist(A, B):
    return (A**2 + B**2)**0.5


def solve(N, lines):
    minDist = INF
    for i in range(N):
        minDist = min(minDist, getDist(*getLastP(N, lines, {i})))
    
    return [getLastP(N, lines, set()), [f"{round(minDist, 20):.2f}"]]


def main():
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(list(map(int, input().split())))
    
    for i in solve(N, lines):
        print(*i)


main()
