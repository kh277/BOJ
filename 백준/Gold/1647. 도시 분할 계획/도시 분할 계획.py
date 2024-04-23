# 백준 1647

'''
마을을 두 개로 분리하고 유지비를 최소로 하기
1. 전체 정점을 대상으로 MST 구하기.
2. 그 뒤, 가장 가중치가 높은 간선 하나 제거하기
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
    total_cost = []

    # 부모 테이블 초기화
    parent = [i for i in range(V+1)]

    # [a, b, cost] 순서에서 cost 기준으로 정렬
    graph.sort(key= lambda x: x[2])

    # 간선을 하나씩 비교
    for i in graph:
        a, b, cost = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost.append(cost)
    
    # 가장 비용이 큰 원소 하나 제거 후 합계 리턴
    total_cost.sort()
    del total_cost[-1]
    return sum(total_cost)


def main():
    V, E = map(int, input().split())
    
    graph = []
    for _ in range(E):
        graph.append(list(map(int, input().split())))
    
    print(kruskal(V, E, graph))


main()