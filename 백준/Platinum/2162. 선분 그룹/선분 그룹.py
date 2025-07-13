# 백준 2162

import io

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
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solve(N, line):
    graph = []
    for i in range(N):
        for j in range(i+1, N):
            if LineIntersection(line[i][0], line[i][1], line[j][0], line[j][1]) == True:
                graph.append([i, j])

    parent = [i for i in range(N)]
    for i in graph:
        a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

    for i in graph:
        a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

    dic = {}
    for num in parent:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

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
