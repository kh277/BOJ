# 백준 6850

'''
문제 설명
소 한 마리당 50m^2의 목초지가 필요하다.
나무의 수 N과 그 나무들의 좌표들이 주어질 때,
이 나무들로 가장 넓은 목초지를 만들 경우 소가 최대 몇 마리 들어갈 수 있는지 출력하기.

Convex Hull로 볼록 껍질을 구성하는 점을 구하고
신발끈 공식을 통해 다각형의 넓이를 구하면 된다.
'''

import sys

input = sys.stdin.readline


# N개의 점으로 이루어진 다각형의 넓이 구하기 - 신발끈 공식
def shoelace_formula(N: int, graph: list) -> float:
    area = 0
    
    for i in range(N):
        j = (i+1) % N
        area += graph[i][0] * graph[j][1]
        area -= graph[i][1] * graph[j][0]
    
    return abs(area) / 2


# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# Convex Hull 구하기
def convex_hull(graph):
    # x좌표 오름차순으로 정렬
    graph = sorted(set(graph))

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


def solve(points: list) -> int:
    # 볼록 껍질 구하기
    hull = convex_hull(points)

    # 해당 볼록 껍질의 넓이 구하기
    return int(shoelace_formula(len(hull), hull) / 50)


def main():
    N = int(input())
    
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    
    print(solve(points))


main()