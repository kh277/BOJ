# 백준 10254

'''
백준 9240번과 유사. 다만, Rotating Calipers 알고리즘이 O(N^2)일 때는 시간초과 발생.
참고 : https://www.cnblogs.com/DreamUp/archive/2010/09/16/1828131.html
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


def output_change(result: list) -> str:
    temp = ""
    for i in result:
        temp += str(i[0]) + " " + str(i[1]) + " "

    return temp


def rotating_calipers(graph: list) -> float:
    # 볼록 껍질 구하기
    hull = convex_hull(graph)
    length = len(hull)

    # 점이 2개 미만인 경우
    if length < 2:
        return 0

    # 점이 2개인 경우
    if length == 2:
        return output_change([hull[0], hull[1]])
    
    result = [0, None, None]
    j = 1

    # 모든 볼록 껍질의 점에 대해
    for i in range(length):
        next_i = (i+1) % length

        # i와 다음 점 next_i을 잇는 직선과 가장 멀리 떨어진 점 도출
        while True:
            next_j = (j+1) % length

            # 벡터의 외적 계산으로 직선으로부터 j와 next_j 까지의 거리 비교
            d1 = cross(hull[i], hull[next_i], hull[j])
            d2 = cross(hull[i], hull[next_i], hull[next_j])

            # next_j가 더 클 경우 갱신
            if d1 < d2:
                j = next_j
            else:
                break
        
        # 최대 거리 갱신
        if result[0] < distance(hull[i], hull[j]):
            result = [distance(hull[i], hull[j]), hull[i], hull[j]]
        elif result[0] < distance(hull[next_i], hull[j]):
            result = [distance(hull[next_i], hull[j]), hull[next_i], hull[j]]
    
    return output_change(result[1:])


def main():
    T = int(input())
    for i in range(T):
        graph = []
        n = int(input())
        for j in range(n):
            a, b = map(int, input().split())
            graph.append((a, b))

        print(rotating_calipers(graph))


main()