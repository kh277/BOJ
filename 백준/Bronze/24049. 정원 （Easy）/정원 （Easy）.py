# 백준 28015

'''
DP[i][j] = [0, i]번째 파이프 중 일부를 사용할 때의 길이가 j일 때, 획득 가능한 최대 용량
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, initY, initX):
    grid = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for y in range(1, N+1):
        grid[y][0] = initY[y-1]
    for x in range(1, M+1):
        grid[0][x] = initX[x-1]
    
    for y in range(1, N+1):
        for x in range(1, M+1):
            grid[y][x] = grid[y-1][x] ^ grid[y][x-1]
    
    return grid[N][M]


def main():
    N, M = map(int, input().split())
    initY = list(map(int, input().split()))
    initX = list(map(int, input().split()))
    print(solve(N, M, initY, initX))


main()
