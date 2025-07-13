# 백준 2162

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 선분 교차 판정 서브 함수
def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# 선분 교차 판정
def LineIntersection(A, B, C, D):
    AB = CCW(A, B, C) * CCW(A, B, D)
    CD = CCW(C, D, A) * CCW(C, D, B)

    if AB == 0 and CD == 0:
        if B < A:
            A, B = B, A
        if D < C:
            C, D = D, C
        return not (B < C or D < A)

    return AB <= 0 and CD <= 0


def find(parent, x):
    root = x
    while parent[root] >= 0:
        root = parent[root]
    
    while x != root:
        nextN = parent[x]
        parent[x] = root
        x = nextN

    return root


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return

    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def solve(N, line):
    # 선분 교차 판정
    graph = []
    for i in range(N):
        for j in range(i+1, N):
            if LineIntersection(line[i][0], line[i][1], line[j][0], line[j][1]) == True:
                graph.append([i, j])

    # 유니온 파인드 작업
    parent = array('i', [-1]) * N
    for a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

    # 그룹 처리
    dic = {}
    for i in range(N):
        root = find(parent, i)
        dic[root] = dic.get(root, 0) + 1

    return [len(dic), max(dic.values())]


def main():
    N = int(input())

    line = []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        line.append([(a, b), (c, d)])
    
    for i in solve(N, line):
        print(i)


main()
