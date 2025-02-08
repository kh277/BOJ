# 백준 4386

'''
모든 별들 간 거리를 구하고 MST를 적용시키면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def kruskal(V, graph):
    total_cost = 0

    parent = [i for i in range(V+1)]
    graph.sort(key= lambda x: x[2])

    for i in graph:
        a, b, cost = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
    
    return total_cost


def solve():
    graph = []

    # 각 별 사이의 거리 저장
    for i in range(N):
        for j in range(N):
            if i != j:
                graph.append([i, j, distance(star[i], star[j])])

    # 크루스칼 진행
    return kruskal(N, graph)/100


# main 함수 ----------
N = int(input())
star = []
for _ in range(N):
    a, b = list(map(float, input().split()))
    star.append([a*100, b*100])

print(solve())