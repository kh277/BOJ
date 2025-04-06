# 백준 6593

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checkRange(x, y, z):
    if 0 <= z < L:
        if 0 <= y < R:
            if 0 <= x < C:
                return True
    
    return False


def BFS(start, end):
    pointX = [-1, 1, 0, 0, 0, 0]
    pointY = [0, 0, -1, 1, 0, 0]
    pointZ = [0, 0, 0, 0, -1, 1]
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(C)]
    
    q = deque()
    q.append([start[0], start[1], start[2], 0])
    visited[start[0]][start[1]][start[2]] = True
    
    while q:
        curZ, curY, curX, curMove = q.popleft()
        
        if grid[curZ][curY][curX] == 'E':
            return curMove
        
        for i in range(6):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            nextZ = curZ + pointZ[i]
            
            if checkRange(nextX, nextY, nextZ) and visited[nextZ][nextY][nextX] == False:
                if grid[nextZ][nextY][nextX] != '#':
                    q.append([nextZ, nextY, nextX, curMove+1])
                    visited[nextZ][nextY][nextX] = True
    
    return -1


def solve():
    start = [0, 0, 0]
    end = [0, 0, 0]
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if grid[z][y][x] == 'S':
                    start = [z, y, x]
                elif grid[z][y][x] == 'E':
                    end = [z, y, x]
    
    result = BFS(start, end)
    return 'Trapped!' if result == -1 else f'Escaped in {result} minute(s).'
                

# main 함수 ----------
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    grid = [[] for _ in range(L)]
    for z in range(L):
        for y in range(R):
            grid[z].append(list(map(str, input().decode().strip())))
        input()

    print(solve())
