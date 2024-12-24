# 백준 7563

'''
폭탄 강도 D가 주어진다. 이 폭탄은 중심과의 좌표 차이가 D 이하의 좌표에 있는 모든 쥐를 죽일 수 있다.
또한 쥐의 개체 수 N이 주어지며, 쥐 각각에 대해 위치 x, y와 개체 수 i가 주어질 때,
쥐를 가장 많이 잡을 수 있는 x, y좌표와 그 때 소멸되는 쥐 개체 수의 합을 구하는 문제이다.

누적 합을 이용해 최적해를 구하자.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MAX = 1025
INF = 10e7


def solve():
    # 1. 계산에 사용할 누적 합 계산
    accSum = [[0 for _ in range(MAX+1)] for _ in range(MAX+1)]

    accSum[0][0] = grid[0][0]

    for x in range(1, MAX+1):
        accSum[0][x] = accSum[0][x-1] + grid[0][x]

    for y in range(1, MAX+1):
        accSum[y][0] = accSum[y-1][0] + grid[y][0]

    for y in range(1, MAX+1):
        for x in range(1, MAX+1):
            accSum[y][x] = grid[y][x] + accSum[y-1][x] + accSum[y][x-1] - accSum[y-1][x-1]

    # 2. 누적 합을 이용해 최대값 탐색
    result = [0, 0, accSum[D][D]]
    for y in range(MAX+1):
        if y-D-1 >= 0:
            curSum = accSum[min(y+D, MAX)][D] - accSum[y-D-1][D]
        else:
            curSum = accSum[min(y+D, MAX)][D]
        if curSum > result[2]:
            result = [0, y, curSum]

    for x in range(MAX+1):
        if x-D-1 >= 0:
            curSum = accSum[D][min(x+D, MAX)] - accSum[D][x-D-1]
        else:
            curSum = accSum[D][min(x+D, MAX)]
        if curSum > result[2]:
            result = [x, 0, curSum]

    for x in range(MAX+1):
        for y in range(MAX+1):
            startX = max(x-D, 1)
            startY = max(y-D, 1)
            endX = min(x+D, MAX)
            endY = min(y+D, MAX)

            curSum = accSum[endY][endX] - accSum[endY][startX-1] - accSum[startY-1][endX] + accSum[startY-1][startX-1]
            if curSum > result[2]:
                result = [x, y, curSum]

    return result


# main 함수 ----------
T = int(input())
for _ in range(T):
    D = int(input())
    N = int(input())
    grid = [[0 for _ in range(MAX+1)] for _ in range(MAX+1)]

    for _ in range(N):
        x, y, i = map(int, input().split())
        grid[y][x] = i

    print(*solve())