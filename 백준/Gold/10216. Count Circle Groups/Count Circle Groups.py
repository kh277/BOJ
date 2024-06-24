# 백준 10216

'''
A_i와 A_j의 넓이가 겹친다면 통신이 가능하다.
따라서 반지름을 통해 두 원이 이어져 있다면 두 정점 사이에 간선이 존재하는 것으로 판단한다.
각 통신탑들 사이에 간선이 존재하는지 확인하고 그래프를 만든 뒤 Union-Find 자료구조를 이용해 탐색한다. 
'''

import sys
import math

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


def solve(N: int, point: list) -> int:
    # 각 통신탑 사이에 간선이 존재하는지 확인
    graph = []
    for i in range(N):
        for j in range(i+1, N):
            distance = (point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2
            R = point[i][2] + point[j][2]
            if distance <= R**2:
                graph.append([i, j])

    # Union-Find 자료구조를 이용해 각 집합의 루트 노드 추출
    root = [i for i in range(N)]
    for i in graph:
        a, b = i
        if find(root, a) != find(root, b):
            union(root, a, b)

    # 직접 비교하지 못한 쌍들끼리 같은 루트를 가지고 있음에도 루트가 아닌 노드를 루트로 인식하고 있을 수 있음.
    # 위 작업 한번 더 반복
    for i in graph:
        a, b = i
        if find(root, a) != find(root, b):
            union(root, a, b)

    # 딕셔너리를 이용해 집합의 원소 개수 파악
    dic = {}
    for num in root:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    return len(dic)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        
        point = []
        for _ in range(N):
            point.append(list(map(int, input().split())))
        
        print(solve(N, point))


main()