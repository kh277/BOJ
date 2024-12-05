# 백준 3679

'''
Monotone Chain 알고리즘에서 하부 Hull만 구한 뒤, 끝점을 기준으로
hull에 없는 점들에 대해 CCW 값을 기준으로 정렬하여 작아지는 순서대로 이으면 된다.
'''

import sys
from functools import cmp_to_key

input = sys.stdin.readline


# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# 점 A, B의 각도 비교
def compare(A, B):
    C = CCW(mark, A, B)
    
    if C == 0:
        return abs(A[0]-mark[0]) + abs(A[1]-mark[1]) < abs(B[1]-mark[0])+abs(B[1]-mark[1])
    
    if C > 0:
        return 1
    
    return 0


# 아래쪽 Convex Hull만 구하기
# Convex Hull을 구성하는 선분 위의 점도 lower에 포함시켜야 함!!
def LowerConvexHull(graph):
    graph.sort(key= lambda x: (x[1], x[0]))

    lower = []
    for i in graph:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) < 0:
            lower.pop()
        lower.append(i)
    
    return lower[:-1]


def solve(N, graph):
    global mark
    # 아래쪽 볼록 껍질 구하기
    lower = LowerConvexHull(graph)
    lowerSet = set(lower)

    # 좌하단 점을 시작점으로 잡기
    mark = [10001, 10001, -1]
    for i in graph:
        if mark[0] > i[0]:
            if mark[1] > i[1]:
                mark = i

    # 시작점을 기준으로 각도순 정렬
    ccwData = []
    for i in range(N):
        if graph[i] not in lowerSet:
            ccwData.append(graph[i])
    ccwData = sorted(ccwData, key=cmp_to_key(compare))

    # 점이 입력된 순서를 resultIndex에 저장
    resultIndex = []
    for i in lower[::-1]:
        resultIndex.append(i[2])

    for i in ccwData:
        resultIndex.append(i[2])

    return resultIndex


# main 함수 ----------
T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    graph = []
    for j in range(data[0]):
        graph.append((data[j*2+1], data[j*2+2], j))

    print(*solve(data[0], graph))

