# 백준 11967

'''
주어진 두 점 스위치 점을 간선으로 생각하자.
그럼 간선들로 그래프를 만들 수 있다.
(1, 1)과 이어진 점의 개수를 하나씩 1로 바꾸면서 접근할 수 있는 방의 개수를 세면 된다.
바꿨는데도 접근할 수 있는 방의 개수가 그대로라면 그 값을 반환하면 된다.

주의 반례
4 6
1 1 2 2
2 2 3 3
3 3 4 4
2 2 1 2
3 3 3 2
4 4 4 3
-> 2
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(data, start):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    result = 1
    
    while q:
        curY, curX = q.popleft()
        
        # cur에 해당하는 좌표에서 불 켜기
        for i in graph[curY][curX]:
            data[i[0]][i[1]] = 1
            result += 1
        
        # cur의 상하좌우 탐색
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            
            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == False:
                if data[nextY][nextX] == 1:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
    
    return result


def solve():
    data = [[0 for _ in range(N)] for _ in range(N)]
    data[0][0] = 1
    
    # 불이 켜지는 방이 수가 달라지지 않을 때까지 반복
    before = -1
    while True:
        lightCount = BFS(data, [0, 0])
        
        # 불이 켜지는 방의 수가 같으면 탈출
        if lightCount == before:
            break
        
        before = lightCount
    
    # 불이 켜진 방의 수 세기
    return sum([sum(data[i]) for i in range(N)])


# main 함수 ----------
N, M = map(int, input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]      # 간선 정보 저장

for _ in range(M):
    x, y, a, b = list(map(int, input().split()))
    graph[y-1][x-1].append([b-1, a-1])


print(solve())