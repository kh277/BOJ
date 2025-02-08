# 백준 15788

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def findZero():
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0:
                return [y, x]


def solve():
    accSum = max(sum(grid[0]), sum(grid[1]))

    # 0의 위치 찾기
    zeroY, zeroX = findZero()
    
    # 0을 제외한 부분의 합이 일정한지 체크
    sumSet = set()
    for y in range(N):
        if y != zeroY:
            temp = 0
            for x in range(N):
                temp += grid[y][x]
            sumSet.add(temp)
    for x in range(N):
        if x != zeroX:
            temp = 0
            for y in range(N):
                temp += grid[y][x]
            sumSet.add(temp)
    if len(sumSet) != 1:
        return -1

    # 가로의 합 도출
    sumX = sum(grid[zeroY])
    addNum = accSum - sumX
    grid[zeroY][zeroX] = addNum

    # 세로 확인
    sumY = 0
    for y in range(N):
        sumY += grid[y][zeroX]
    if sumY != accSum:
        return -1

    # 대각선 확인
    sumXY = 0
    sumYX = 0
    for y in range(N):
        sumXY += grid[y][y]
        sumYX += grid[N-1-y][y]
    if sumXY != accSum or sumYX != accSum:
        return -1
    
    return addNum


# main 함수 ----------
N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

print(solve())