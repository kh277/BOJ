# 백준 30416

'''
최대한 다른 사각형을 많이 포함하는 사각형을 구하는 문제이다.
1 <= N <= 75이므로 브루트포스를 사용하여 풀어도 된다.

볼록 다각형은 이미 주어져 있으므로,
한 도형을 기준으로 다른 도형의 네 점이 전부 이 도형의 내부에 있으면 포함하고 있는 것이다.
점을 반시계 방향으로 정렬하고 볼록 다각형 내부의 점 판정을 이용하여 계산하자.
'''

import sys
import math

input = sys.stdin.readline

def CCW(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def point_in_polygon(point: tuple, hull: list) -> bool:

    # 1번과 n-1번 반직선 사이에 점이 존재하지 않는 경우
    if CCW(hull[0], hull[-1], point) > 0:
        return False
    if CCW(hull[0], hull[1], point) < 0:
        return False

    # 이분 탐색으로 두 직선 구하기
    left = 1
    right = len(hull) - 1
    while left < right:
        mid = (left + right) // 2
        if CCW(hull[0], hull[mid], point) > 0:
            left = mid + 1
        else:
            right = mid

    # 최종적으로 남은 left와 left-1 사이에 점이 있는지 확인
    return CCW(hull[left-1], hull[left], point) >= 0


def sort_point(points):
    center = [sum([p[0] for p in points]) / len(points), sum([p[1] for p in points]) / len(points)]
    return sorted(points, key=lambda p: math.atan2(p[1]-center[1], p[0]-center[0]))


def solve(N: int, hull: list) -> int:
    # 다른 상자를 포함하는 갯수를 저장할 리스트
    result = [0 for _ in range(N)]

    # 반시계 방향으로 정렬
    for i in range(N):
        hull[i] = sort_point(hull[i])

    # 모든 도형에 대해 반복
    for i in range(N):
        for j in range(N):
            count = 0
            # j번째 도형의 네 점이 i번째 도형의 내부에 있는지 판단
            for k in range(4):
                if point_in_polygon(hull[j][k], hull[i]):
                    count += 1
            if count == 4:
                result[i] += 1

    return max(result)


def main():
    N = int(input())

    hull = [[] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(4):
            hull[i].append([temp[j*2], temp[j*2+1]])

    print(solve(N, hull))

main()