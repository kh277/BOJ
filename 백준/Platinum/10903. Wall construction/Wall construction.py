# 백준 10903

'''
최소한의 유리를 이용하여 모든 기둥을 포함하는 외벽 만들기
-> 기둥들이 이루는 도형의 둘레 + 원기둥의 둘레
-> Convex Hull을 구하고 2*pi*r을 둘레의 길이에 더하자.
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


# 두 점 사이의 거리
def length(a: list, b: list) -> float:
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def solve(N: int, R: int, graph: list) -> float:
    hull = convex_hull(graph)

    result = 0
    
    # Convex Hull을 이루는 기둥들의 둘레
    for i in range(len(hull)):
        next_i = (i+1)%len(hull)
        result += length(hull[i], hull[next_i])

    # 원기둥의 둘레
    result += 2 * R * math.pi

    return result


def main():
    N, R = map(int, input().split())
    
    graph = []
    for i in range(N):
        graph.append(tuple(map(int, input().split())))
    
    print(solve(N, R, graph))


main()