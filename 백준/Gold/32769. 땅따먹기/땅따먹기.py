# 백준 32769

'''
그래프에 주어진 1~20까지의 수를 학생 A, B, C에게 배정해야 한다.
다만, 1의 영역과 2의 영역이 서로 인접해 있다면 1과 2는 다른 사람에게 배정되어야 한다.
따라서 각 영역과 인접한 땅을 간선으로 저장하여 탐색하자.
'''

import sys
from collections import deque

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


# BFS : start가 속한 영역과 인접한 영역 체크 
def BFS(start, data, visited):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    curNum = graph[start[0]][start[1]]

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N:
                # 같은 영역일 경우 -> BFS 탐색
                if graph[nextY][nextX] == curNum and visited[nextY][nextX] == False:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
                # 다른 영역일 경우 -> 인접 영역 숫자 저장
                elif graph[nextY][nextX] != curNum:
                    data[curNum].add(graph[nextY][nextX])

    return


# 백트래킹 : curArea번 영역을 player가 가지게 될 경우 체크
def backtrack(curArea, curPlayer, data, host):
    # 종료조건
    if curArea > maxNum:
        return True
    
    # curPlayer가 curArea를 차지해도 되는지 체크
    for i in data[curArea]:
        # curArea번째 영역의 소유자와 host[i]번째 영역의 소유자가 같은 경우 -> 영역 배정 불가
        if host[i] == curPlayer:
            return False
    host[curArea] = curPlayer

    # 다음 영역 재귀
    for nextPlayer in range(3):
        if backtrack(curArea+1, nextPlayer, data, host) == True:
            return True
    
    # 탐색에 실패한 경우, 이전 상태로 복구
    host[curArea] = -1
    return False


def solve():
    data = [set() for _ in range(maxNum+1)]     # 각 영역과 이웃한 영역 저장
    visited = [[False for _ in range(M)] for _ in range(N)]     # graph 방문 처리

    # 각 영역과 인접한 영역 체크
    for y in range(N):
        for x in range(M):
            if visited[y][x] == False:
                BFS([y, x], data, visited)

    # set -> list
    for i in range(maxNum+1):
        data[i] = sorted(list(data[i]))

    # 백트래킹를 통해 각 영역에 주인을 할당할 때 에러가 생기는지 체크
    return 'Not Sure' if backtrack(1, 0, data, [-1 for _ in range(maxNum+1)]) == True else 'Wrong'


# main 함수 ----------
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

maxNum = max([max(i) for i in graph])

print(solve())
