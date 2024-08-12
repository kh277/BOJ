# 백준 20303

'''
한 아이의 사탕을 뺏으면 그 아이와 친구인 모든 친구들의 사탕을 뺏게 된다.
따라서 서로 이어진 아이들의 수를 무게(W)로,
서로 이어진 아이들이 가진 사탕의 총합을 가치(V)로 표현한다.

스브러스가 최대로 뺏을 수 있는 사탕의 수를 구하는 것이므로
무게 제한이 K인 가방 속에 V가 최대가 되도록 하는 경우를 구하는 배낭 문제와 같다.
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
    
    return


def union_find(N: int, K: int, candy: list, data: list) -> list:
    # Union-Find 자료구조를 이용해 각 집합의 루트 노드 추출
    root = [i for i in range(N+1)]
    for i in data:
        a, b = i
        if find(root, a) != find(root, b):
            union(root, a, b)

    # 직접 비교하지 못한 쌍들끼리 같은 루트를 가지고 있음에도 루트가 아닌 노드를 루트로 인식하고 있을 수 있음.
    # 위 작업 한번 더 반복
    for i in data:
        a, b = i
        if find(root, a) != find(root, b):
            union(root, a, b)

    # 딕셔너리를 이용해 집합의 원소 개수 파악
    dic = {}
    for i in range(1, len(root)):
        if root[i] in dic:
            dic[root[i]] = [dic[root[i]][0]+1, dic[root[i]][1]+candy[i-1]]
        else:
            dic[root[i]] = [1, candy[i-1]]
    
    graph = []
    for i in dic:
        graph.append(dic[i])
    
    return graph


def knapsack(N: int, K: int, bag: list):
    DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # 물건 순서대로 탐색
    # i: 현재 탐색하는 물건 번호
    for i in range(1, N+1):
        cur_weight, cur_value = bag[i-1]
        # 현재 무게에 해당 물건을 넣고 갱신할 수 있는 경우 넣기
        # j: 현재 탐색하는 무게
        for j in range(1, K+1):
            # cur 물건을 넣는 경우
            if j-cur_weight >= 0:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j-cur_weight]+cur_value, DP[i-1][j])
            # cur 물건을 넣지 않는 경우
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])

    return DP[N][K]


def solve(N: int, K: int, candy: list, data: list) -> int:
    # 1. 분리 집합을 이용해 서로 연결된 아이들을 구함
    graph = union_find(N, K, candy, data)

    # 2. 배낭 문제 해결
    return knapsack(len(graph), K-1, graph)


def main():
    N, M, K = map(int, input().split())
    candy = list(map(int, input().split()))

    data = []
    for _ in range(M):
        data.append(list(map(int, input().split())))

    print(solve(N, K, candy, data))


main()