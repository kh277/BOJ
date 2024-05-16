# 백준 2887

'''
N개의 정점에 대한 좌표가 주어지고,
이 N개의 점을 최소 가중치로 잇는 최소 신장 트리를 구하는 문제이다.

다만, N개의 정점에 대한 정보만 주어지고 각 정점 사이의 노드에 대한 정보는 직접 구해야 한다.
모든 정점에서 노드를 고려할 경우 O(N^2)의 시간복잡도가 걸리게 된다.
따라서 여러 노드 중 답이 될 가능성이 있는 노드를 추출한다.
그 뒤, 노드들에 대해 최소 신장 트리를 만들면 된다.

두 좌표 간 x좌표의 차이, y좌표의 차이, z좌표의 차이의 최소값이 가중치가 된다.
따라서 x좌표, y좌표, z좌표를 오름차순으로 정렬해보자.
먼저, x좌표를 기준으로 보면,
오름차순 정렬된 첫 번째 정점(A)과 두 번째 정점(B)의 차이가 A좌표에서 x좌표 차이가 적은 점이 된다.
또한, 정렬된 두 번째 정점(B)이 세 번째 정점(C) 최소값이 B에서 x좌표 차이가 가장 적은 점이 된다.

위 과정을 N-1번째 점까지 반복하면, 총 반복 횟수는 3N이 되게 되어 O(N)만에 경로를 구할 수 있게 된다.
그 뒤, Kruskal 알고리즘을 이용하여 최소 신장 트리를 구하면 된다.
'''

import sys

input = sys.stdin.readline


def find(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent: list, a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(V: int, E: int, graph: list) -> int:
    total_cost = 0

    # 부모 테이블 초기화
    parent = [i for i in range(V+1)]

    # [a, b, cost] 순서에서 cost 기준으로 정렬
    graph.sort(key= lambda x: x[2])

    # 간선을 하나씩 비교
    for i in graph:
        a, b, cost = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
    
    return total_cost


def solve(N: int, loc: list):
    # 각 좌표에 대해 오름차순 정렬
    xList = sorted(loc, key= lambda x: x[0])
    yList = sorted(loc, key= lambda x: x[1])
    zList = sorted(loc, key= lambda x: x[2])

    # 최소값이 갱신 가능한 경우 갱신
    # data에 [시작 정점, 도착 정점, 가중치] 순으로 저장
    data = []
    for i in range(1, N):
        data.append([xList[i-1][3], xList[i][3], xList[i][0]-xList[i-1][0]])
        data.append([yList[i-1][3], yList[i][3], yList[i][1]-yList[i-1][1]])
        data.append([zList[i-1][3], zList[i][3], zList[i][2]-zList[i-1][2]])

    # 각 좌표에 대해 중복값이 존재할 수 있으므로 딕셔너리에 키:값 형태로 저장 후 중복 제거
    temp = {}
    for start, end, cost in data:
        key = (start, end)
        
        if key not in temp or cost < temp[key]:
            temp[key] = cost
    
    graph = [[start, end, cost] for (start, end), cost in temp.items()]

    # graph에 대해 Kruskal 알고리즘 적용
    return kruskal(N, len(graph), graph)


def main():
    N = int(input())
    
    # [[x좌표1, y좌표1, z좌표1, 1], [x좌표2, y좌표2, z좌표2, 2], ...] 순으로 저장
    # 맨 마지막에는 각 정점의 번호를 저장함
    loc = []
    for i in range(N):
        loc.append(list(map(int, input().split())) + [i])
    
    print(solve(N, loc))


main()