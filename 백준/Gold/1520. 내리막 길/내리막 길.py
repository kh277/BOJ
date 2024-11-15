# 백준 1520

'''
재귀를 통해 탑다운 DP 방식으로 탐색하자.
'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def DFS(start):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    # 재귀 종료 조건
    if start == [0, 0]:
        return 1
    
    # 상하좌우 좌표에 대해 재귀
    result = 0
    for i in range(4):
        nextX = start[1] + pointX[i]
        nextY = start[0] + pointY[i]
    
        if 0 <= nextX < N and 0 <= nextY < M:
            if graph[nextY][nextX] > graph[start[0]][start[1]]:
                if DP[nextY][nextX] != -1:
                    result += DP[nextY][nextX]
                else:
                    result += DFS([nextY, nextX])
    
    DP[start[0]][start[1]] = result
    return result


# main 함수 ----------
M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

DP = [[-1 for _ in range(N)] for _ in range(M)]
print(DFS([M-1, N-1]))