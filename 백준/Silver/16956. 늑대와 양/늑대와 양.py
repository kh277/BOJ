# 백준 16956

import sys

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def BFS(start):
    curY = start[0]
    curX = start[1]
    
    for i in range(4):
        nextX = curX + pointX[i]
        nextY = curY + pointY[i]

        if 0 <= nextX < M and 0 <= nextY < N:
            if grid[nextY][nextX] == 'S':
                continue
            elif grid[nextY][nextX] == 'W':
                return False
            else:
                grid[nextY][nextX] = 'D'
    
    return True


def solve():
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'S':
                if BFS([y, x]) == False:
                    return [0]


    return [1] + [''.join(i) for i in grid]


# main 함수 ----------
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

for i in solve():
    print(i)