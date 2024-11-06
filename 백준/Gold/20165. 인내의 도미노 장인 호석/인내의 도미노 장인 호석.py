# 백준 20165

import sys
from collections import deque

input = sys.stdin.readline

def solve(attack, defence):
    score = 0
    way = dict()
    way['N'] = [-1, 0]
    way['S'] = [1, 0]
    way['E'] = [0, 1]
    way['W'] = [0, -1]

    # 공격 처리
    q = deque()
    # 큐에 [y좌표, x좌표, 공격 방향, 공격 범위] 순서로 저장
    q.append([int(attack[0])-1, int(attack[1])-1, attack[2], graph[int(attack[0])-1][int(attack[1])-1]])
    graph[int(attack[0])-1][int(attack[1])-1] *= -1
    score += 1

    while q:
        curY, curX, attackWay, attackRange = q.popleft()
        for i in range(1, attackRange):
            nextX = curX + way[attackWay][1]*i
            nextY = curY + way[attackWay][0]*i
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] > 0:
                q.append([nextY, nextX, attackWay, graph[nextY][nextX]])
                graph[nextY][nextX] *= -1
                score += 1

    # 수비 처리
    if graph[defence[0]-1][defence[1]-1] < 0:
        graph[defence[0]-1][defence[1]-1] *= -1

    return score


def change(graph):
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                graph[y][x] = 'S'
            else:
                graph[y][x] = 'F'
    
    return graph


# main 함수 ----------
N, M, R = map(int, input().split())
graph = []
score = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(R):
    attack = list(map(str, input().split()))
    defence = list(map(int, input().split()))

    score += solve(attack, defence)

print(score)
for i in change(graph):
    print(*i)