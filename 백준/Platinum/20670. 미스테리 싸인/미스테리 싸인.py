# 백준 20670

'''
A 다각형과 B 다각형 사이에 모든 점이 존재하는지 확인하는 문제이다.
점의 수는 최대 30만개이므로 O(NlogN)으로 해결해야 한다.

-> 시간복잡도가 O(NlogN)인 내부 점 판정 알고리즘을 사용한다.
'''

import sys

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
    return CCW(hull[left-1], hull[left], point) > 0


def solve(hull_A: list, hull_B: list, point: list) -> str:
    count = 0
    for i in point:
        # A 외부에 있거나 B 내부에 있는 경우
        if point_in_polygon(i, hull_A) == False or point_in_polygon(i, hull_B) == True:
            count += 1

    if count == 0:
        return "YES"
    else:
        return str(count)


def main():
    N, M, K = map(int, input().split())
    
    hull_A = []
    A = list(map(int, input().split()))
    for i in range(N):
        hull_A.append((A[2*i], A[2*i+1]))
    
    hull_B = []
    B = list(map(int, input().split()))
    for i in range(M):
        hull_B.append((B[2*i], B[2*i+1]))
    
    point = []
    p = list(map(int, input().split()))
    for i in range(K):
        point.append((p[2*i], p[2*i+1]))
    
    print(solve(hull_A, hull_B, point))


main()