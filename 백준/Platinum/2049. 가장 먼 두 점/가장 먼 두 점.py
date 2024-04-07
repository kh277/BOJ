# 백준 2049

'''
볼록 껍질을 구성하는 점을 구하고 회전하는 캘리퍼스를 이용해 두 점 사이의 거리의 최대값을 구한다.
'''


import sys

input = sys.stdin.readline


def cross(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def distance(a: list, b: list) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def convex_hull(graph):

    # 구성하는 점이 3개 미만일 경우
    if len(graph) < 3:
        return graph

    # x좌표 오름차순으로 정렬
    graph = sorted(set(graph))

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


def rotating_calipers(graph: list) -> int:
    hull = convex_hull(graph)
    length = len(hull)

    # 점이 2개 미만인 경우
    if length < 2:
        return 0

    # 점이 2개인 경우
    if length == 2:
        return distance(hull[0], hull[1])
    
    max_distance = 0
    
    # hull의 모든 점들에 대해 비교하여 최장 거리 도출
    for i in range(length):
        for j in range(i+1, length):
            max_distance = max(max_distance, distance(hull[i], hull[j]))
    
    # 최대 거리 반환
    return max_distance


def main():
    n = int(input())
    graph = []
    
    for i in range(n):
        graph.append(tuple(map(int, input().split())))
    
    # 중복 점 제거
    print(rotating_calipers(list(set(graph))))


main()