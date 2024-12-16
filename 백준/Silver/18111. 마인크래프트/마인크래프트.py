# 백준 18111

import sys

input = sys.stdin.readline
INF = 10e10


def solve():
    maxValue = max([max(x) for x in grid])
    minValue = min([min(x) for x in grid])
    gridSum = sum([sum(x) for x in grid])
    time = INF
    height = 0
    
    for curHeight in range(minValue, maxValue+1):
        # 높이를 전부 curHeight로 만들 수 있는 경우
        curTime = 0
        if gridSum + B - curHeight*N*M >= 0:
            # 필요한 시간 측정
            for y in range(N):
                for x in range(M):
                    if grid[y][x] > curHeight:
                        curTime += 2 * (grid[y][x] - curHeight)
                    elif grid[y][x] < curHeight:
                        curTime += (curHeight - grid[y][x])

            # time을 갱신 가능한지 확인
            if time > curTime:
                time = curTime
                height = curHeight
            elif time == curTime:
                height = max(height, curHeight)
    
    return [time, height]


# main 함수 ----------
N, M, B = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

print(*solve())