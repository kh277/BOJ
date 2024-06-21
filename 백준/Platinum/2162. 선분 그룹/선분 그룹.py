# 백준 2162

'''
N <= 3000이므로 O(N^2)으로 풀 수 있다.

시도1
서로 교차하는 선분들끼리 같은 집합에 넣어둔다.
어느 선분과도 교차하지 않으면 새로운 집합을 만들어 넣어둔다.
-> 선분1과 선분3이 이어지고 선분2와 선분3이 이어지는 경우
2개의 그룹으로 표시되는 문제가 발생한다.


시도2
Union-Find 자료구조를 이용해서 선분 집합을 구현한다.
선분을 정점으로, 선분 교차 판정을 간선으로 생각하여 각각에 대한 집합을 구한다.
'''

import sys
from collections import deque

input = sys.stdin.readline


# 선분 교차 판정 알고리즘 ----------
# 이차원 좌표 A, B 사이에 check값이 존재하는지 확인
def check_range(A: list, B: list, check: list) -> bool:
    # 정의역과 치역에 대해 확인
    for i in range(2):
        if not min(A[i], B[i]) <= check[i] <= max(A[i], B[i]):
            return False
    
    return True


# 두 점 A, B를 입력받아 ax + by = c의 계수 a, b, c를 리턴하는 함수
def coef(A: list, B: list) -> list:
    if A[0] == B[0]:
        return [1, 0, A[0]]
    elif A[1] == B[1]:
        return [0, 1, A[1]]
    else:
        return [B[1]-A[1], A[0]-B[0],  (B[1]-A[1])*A[0] - (B[0]-A[0])*A[1]]


# 크래머 공식을 이용하여 선분 교차 판정
def line_segment_intetsection(A: list, B: list, C: list, D: list) -> int:
    # ax + by = e, cx + dy = f 꼴의 연립일차방정식 도출
    a, b, e = coef(A, B)
    c, d, f = coef(C, D)

    # 도출한 연립일차방정식의 해 판정
    det = a*d - b*c

    # 해가 없거나 무수히 많은 경우
    if det == 0:
        # 두 선분이 일치하는 경우
        if e == f:
            # 두 선분의 정의역이 겹치면 교차 판정
            if check_range(A, B, C) or check_range(A, B, D) or check_range(C, D, A) or check_range(C, D, B):
                return 1
            else:
                return 0
        
        # 두 선분이 평행하는 경우
        else:
            return 0

    # 해가 존재하는 경우
    x = (e*d-b*f) / det
    y = (a*f-e*c) / det

    # 해가 선분 위에 존재하는지 확인
    if check_range(A, B, [x, y]) and check_range(C, D, [x, y]):
        return 1
    else:
        return 0


# Union-Find 자료구조 ----------
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


def solve(N: int, line: list):
    # 각 선분을 정점으로 보면서 교차하는 경우 간선이 존재한다고 생각함.
    graph = []
    for i in range(N):
        for j in range(i+1, N):
            if line_segment_intetsection(line[i][0], line[i][1], line[j][0], line[j][1]):
                graph.append([i, j])
    
    # Union-Find 자료구조를 이용해 각 집합의 루트 노드 추출
    parent = [i for i in range(N)]
    for i in graph:
        a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    
    # 직접 비교하지 못한 쌍들끼리 같은 루트를 가지고 있음에도 루트가 아닌 노드를 루트로 인식하고 있을 수 있음.
    # 위 작업 한번 더 반복
    for i in graph:
        a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    
    # 딕셔너리를 이용해 집합의 원소 개수 파악
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
        line.append([[a, b], [c, d]])
    
    for i in solve(N, line):
        print(i)


main()
