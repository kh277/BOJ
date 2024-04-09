# 백준 7420

'''
주어진 점들로부터 L 이상의 거리를 두면서, 방벽의 길이가 최소가 되게 해야 한다.
따라서, 볼록 껍질을 구한 뒤 그 점들을 구성하는 길이 + 반지름이 L인 원의 둘레를 구하면 된다.

주의해야 할 점은, 세 점이 한 직선상에 있을 수 있다는 점이다.
'''

import sys
import math

input = sys.stdin.readline

# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def cross(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# 두 점 사이의 거리 구하기
def distance(a: list, b: list) -> int:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Convex Hull 구하기
def convex_hull(graph):
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


def solve(N: int, L: int, graph: list) -> int:
    hull = convex_hull(graph)
    result = 0

    for i in range(len(hull)):
        next_i = (i + 1) % len(hull)
        result += distance(hull[i], hull[next_i])
    
    result += math.pi * 2 * L

    return round(result)


def main():
    N, L = map(int, input().split())
    graph = []

    for i in range(N):
        graph.append(tuple(map(int, input().split())))
    
    print(solve(N, L, graph))


main()
