# 백준 9240

'''
n개의 점에서 가장 멀리 떨어진 두 점 구하기
-> Convex Hull을 구하고 Rotating Calipers를 이용해 최장 거리를 가진 두 점 구하기

주의 반례 -> 처음 탐색하는 i, next_i가 최대값인 경우
5
0 0
100 1
2 10
1 10
0 9

주의 반례2 -> 탐색 과정 중 i와 j의 거리가 줄어든 뒤 최대값이 나오는 경우 
참고 : https://www.cnblogs.com/Booble/archive/2011/04/03/2004865.html
5
8 6
4 9
2 1
7 7
0 6
'''

import sys
import math

input = sys.stdin.readline


def cross(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(graph):
    # x좌표 오름차순으로 정렬
    graph = sorted(set(graph))

    # 점이 1개 이하인 경우
    if len(graph) <= 1:
        return graph

    # 아래쪽 Hull을 구함
    lower = []
    for i in graph:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
        
    # 위쪽 Hull을 구함
    upper = []
    for i in reversed(graph):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    
    # 아래쪽 Hull과 위쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]


def distance(a: list, b: list) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def rotating_calipers(graph: list) -> float:
    hull = convex_hull(graph)
    length = len(hull)

    # 점이 2개 미만인 경우
    if length < 2:
        return 0

    # 점이 2개인 경우
    if length == 2:
        return math.sqrt(distance(hull[0], hull[1]))
    
    max_distance = 0
    
    # hull의 모든 점들에 대해 비교하여 최장 거리 도출
    for i in range(length):
        for j in range(i+1, length):
            max_distance = max(max_distance, distance(hull[i], hull[j]))
    
    # 최대 거리 반환
    return math.sqrt(max_distance)


def main():

    graph = []
    C = int(input())
    for j in range(C):
        a, b = map(int, input().split())
        graph.append((a, b))

    print(rotating_calipers(graph))


main()