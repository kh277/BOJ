# 백준 27656

'''
주어진 점들에 대해 가장 바깥쪽 볼록 껍질을 구하고 그 점들을 제외시킨다.
남겨진 점들에 대해 볼록 껍질을 구하고 그 점들을 제외시킨다.
...
위 과정을 반복해서 각 껍질을 이루는 점들을 구하고,
가장 바깥쪽 껍질부터 다각형 내부 판정을 통해 도형의 내부에 화살이 있는지 체크한다.
'''

import sys

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
    # 등호를 추가하여 선분 위에 존재하는 경우도 포함
    return CCW(hull[left-1], hull[left], point) >= 0


def solve(N: int, points: list, Q: int, arrow: list) -> list:
    left_points = points

    # 볼록 껍질 분리
    hull = []
    while True:
        # 볼록 껍질을 구한 뒤 그 점을 hull에 추가
        cur_hull = convex_hull(left_points)
        hull.append(cur_hull)

        # 볼록 껍질에 속하지 않은 점 left_point에서 제거
        for i in set(cur_hull):
            left_points.remove(i)
        
        # 탈출조건
        if len(left_points) == 0:
            break
    
    # 화살 좌표 처리
    result = [0 for _ in range(Q)]
    for i in range(Q):
        # 껍질이 1개인 경우
        if len(hull) == 1:
            if point_in_polygon(arrow[i], hull[0]) == True:
                result[i] = 1
            else:
                result[i] = 0
            continue

        # 이분 탐색으로 껍질 내부 점 판단
        start = 0
        end = len(hull)
        while True:
            mid = (start + end) // 2
            
            # 이분 탐색 종료 조건
            if end - start <= 1:
                if point_in_polygon(arrow[i], hull[start]) == True:
                    result[i] = start+1
                elif point_in_polygon(arrow[i], hull[end]) == True:
                    result[i] = end+1
                else:
                    result[i] = start
                break
            
            # 범위 절반으로 줄이기
            if point_in_polygon(arrow[i], hull[mid]) == True:
                start = mid
            else:
                end = mid

    return result


def main():
    # 입력 처리
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    
    Q = int(input())
    arrow = []
    for _ in range(Q):
        arrow.append(tuple(map(int, input().split())))
    
    # 결과 출력
    for i in solve(N, points, Q, arrow):
        print(i)


main()