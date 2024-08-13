# 백준 20040

'''
그래프에서 사이클을 판별하려면 분리 집합을 이용하자.
간선 AB가 입력될 때, find 연산으로 A와 B의 부모 노드를 찾는다.
부모 노드가 같다면 사이클이 발생한 것이고 다르다면 사이클이 발생하지 않은 것이다. 
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


def solve(V: int, graph: list) -> int:
    cycle = 0

    parent = [i for i in range(V)]

    # 각 간선에 대해 반복
    for cur in graph:
        cycle += 1
        a, b = cur

        # 사이클이 생기는 경우
        if find(parent, a) == find(parent, b):
            return cycle
        
        union(parent, a, b)
    
    # 사이클이 생기지 않는 경우 
    return 0


def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(M):
        graph.append(list(map(int, input().split())))
    
    print(solve(N, graph))


main()