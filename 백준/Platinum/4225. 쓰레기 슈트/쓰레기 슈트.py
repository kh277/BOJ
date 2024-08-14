# 백준 4225

'''
어떤 다각형이 주어질 때, 이 다각형이 통과할 수 있는 통로 너비의 최소값을 구하는 문제이다.

다각형이 오목 다각형일 수도 있고, 오목 부분은 통로를 지나는 데 신경쓰지 않아도 된다.
따라서 볼록 껍질을 구하고, 볼록 껍질 위의 인접한 두 점을 연결한 직선과 가장 멀리 떨어진 점 사이의 거리를 구한다.
볼록 껍질의 다른 모든 변에 대해 반복한 뒤 이 값들의 최소값을 출력하면 된다.
'''

import sys
import math

input = sys.stdin.readline


# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# Convex Hull 구하기
def convex_hull(graph):
    # x좌표 오름차순으로 정렬
    graph = sorted(graph)

    # 아래쪽 Hull을 구함
    lower = []
    for i in graph:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
        
    # 위쪽 Hull을 구함
    upper = []
    for i in reversed(graph):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    
    # 아래쪽 Hull과 위쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]


# 두 점 A, B를 입력받아 ax + by = c의 계수 a, b, c를 리턴하는 함수
def coef(A: list, B: list) -> list:
    if A[0] == B[0]:
        return [1, 0, A[0]]
    elif A[1] == B[1]:
        return [0, 1, A[1]]
    else:
        return [B[1]-A[1], A[0]-B[0],  (B[1]-A[1])*A[0] - (B[0]-A[0])*A[1]]


# 점 P(x, y)과 직선(ax+by=c) 사이의 거리 리턴
def distance(P: list, a: int, b: int, c: int) -> float:
    return abs(a*P[0]+b*P[1]-c) / math.sqrt(a**2+b**2)


def solve(N: int, points: list) -> float:
    hull = convex_hull(points)

    result = []

    for cur in range(len(hull)):
        next = (cur+1)%len(hull)
        
        # cur과 next를 지나는 직선 구하기
        a, b, c = coef(hull[cur], hull[next])

        # 직선과 각 꼭짓점 사이의 최대값 구하기
        max_range = 0
        for i in hull:
            max_range = max(max_range, distance(i, a, b, c))
        
        result.append(max_range)

    # 점과 직선 사이의 최대 거리값들 중 최소값 리턴
    # 올림하여 소수점 둘째 자리까지 출력
    return f"{math.ceil(min(result) * 100) / 100:.2f}"


def main():
    count = 1
    while True:
        N = int(input())
        if N == 0:
            break
        
        points = []
        for _ in range(N):
            points.append(tuple(map(int, input().split())))
        
        print("Case {x}: {y}".format(x=count, y=solve(N, points)))
        count += 1


main()