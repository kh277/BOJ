# 백준 1197

'''
최소 신장 트리를 구하는 알고리즘인 Kruskal 알고리즘을 이용하자.
'''


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


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


def main():
    V, E = map(int, input().split())
    graph = []

    for _ in range(E):
        graph.append(list(map(int, input().split())))

    print(kruskal(V, E, graph))

main()