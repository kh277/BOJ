# 백준 14066

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

block = [
    [None, None, '+', '-', '-', '-', '+'],
    [None, '/', ' ', ' ', ' ', '/', '|'],
    ['+', '-', '-', '-', '+', ' ', '|'],
    ['|', ' ', ' ', ' ', '|', ' ', '+'],
    ['|', ' ', ' ', ' ', '|', '/'],
    ['+', '-', '-', '-', '+']]


def makeBlock(sY, sX, grid):
    curY = sY-5
    for i in block:
        curX = sX
        for j in i:
            if j != None:
                grid[curY][curX] = j
            curX += 1
        curY += 1


def solve(Y, X, data):
    # 가능한 최대 x, y, z 체크
    maxZ = 0
    maxY = 5
    maxX = 4*X + 2*Y + 1
    for y in data:
        maxZ = max(maxZ, max(y))
    for y in range(Y-1, -1, -1):
        z = max(data[y])
        needY = 3*z + 3 + 2*(Y-1 - y)
        maxY = max(maxY, needY)

    # 격자에 z+, y+, x+ 순서대로 배치
    grid = [['.'] * maxX for _ in range(maxY)]
    for z in range(1, maxZ+1):
        for y in range(Y):
            for x in range(X):
                if data[y][x] >= z:
                    startY = maxY-1 - 2*(Y-y-1) - 3*(z-1)
                    startX = 2*(Y-y+1) + 4*x - 4
                    makeBlock(startY, startX, grid)
    return grid


def main():
    Y, X = map(int, input().decode().split())
    data = []
    for _ in range(Y):
        data.append(list(map(int, input().split())))
    for i in solve(Y, X, data):
        print(''.join(i))


main()
