# 백준 16716

'''
저격 장소에서 저격을 했을 때 한 번에 잡을 수 있는 적의 번호를 묶어서 저장해둔다.
N이 최대 20이므로 2^20개의 가짓수를 전부 체크하여 총알 수를 계산하는 방법으로 해결할 수 있다.

방문 처리를 비트마스킹으로 처리하고, 재귀를 이용해 가짓수를 처리하면 된다.
방문한 정점은 0, 방문하지 않은 정점은 1로 처리한다.
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# dx, dy의 변화량을 서로소가 1이 되도록 약분
def delta(dx, dy):
    if dx == 0 and dy == 0:
        return (0, 0)
    gcd = math.gcd(dx, dy)

    return dx // gcd, dy // gcd


# 위치 curPoint에서 저격할 때 동시에 잡을 수 있는 적을 그래프로 묶기 
def addPoint(curPoint):
    dic = dict()
    curX, curY = curPoint
    for i in range(N):
        enemyX, enemyY = enemy[i]
        dx, dy = delta(enemyX - curX, enemyY - curY)
        if (dx, dy) in dic:
            dic[(dx, dy)].add(i)
        else:
            dic[(dx, dy)] = {i}

    graph = [set() for _ in range(N)]
    for i in dic:
        for j in dic[i]:
            graph[j].update(dic[i])

    return graph


def recur(statusA, statusB, snipeCount):
    # 아직 저격되지 않은 가장 낮은 정점을 다음 저격 정점으로 선택
    nextV = -1
    for i in range(N):
        if (statusA & (1 << i)) & (statusB & (1 << i)):
            nextV = i
            break

    # 모든 정점이 처리된 경우
    if nextV == -1:
        if maxData[0] > snipeCount:
            maxData[0] = snipeCount
            if statusA == 0:
                maxData[1] = 0
            else:
                maxData[1] = 1
        elif maxData[0] == snipeCount and statusA == 0:
            maxData[1] = 0
        return

    # A번 자리에서 nextV 쪽으로 저격하는 경우
    nextA = statusA
    for i in graphA[nextV]:
        nextA = nextA & ~(1 << i)
    recur(nextA, statusB, snipeCount+1)

    # B번 자리에서 nextV 쪽으로 저격하는 경우
    nextB = statusB
    for i in graphB[nextV]:
        nextB = nextB & ~(1 << i)
    recur(statusA, nextB, snipeCount+1)


def solve():
    global graphA, graphB

    # 한번에 처리할 수 있는 정점 묶기
    graphA = addPoint(point[0])
    graphB = addPoint(point[1])

    # 재귀 처리
    recur((1<<N) - 1, (1<<N) - 1, 0)


# main 함수 ----------
N = int(input())
enemy = []
for _ in range(N):
    enemy.append(list(map(int, input().split())))
point = []
for _ in range(2):
    point.append(list(map(int, input().split())))
maxData = [100, 1]        # [사용한 총알 수, 자리 이동 횟수]

solve()
print(*maxData)
