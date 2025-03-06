# 백준 2049

'''
볼록 껍질을 구성하는 점을 구하고 회전하는 캘리퍼스를 이용해 두 점 사이의 거리의 최대값을 구한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def distance(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


def ConvexHull(points):
    # x좌표 오름차순으로 정렬
    points = sorted(set(points))

    # 아래쪽 Hull 구하기
    lower = []
    for point in points:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    # 위쪽 Hull 구하기
    upper = []
    for point in reversed(points):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    # 아래쪽 Hull과 위쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]


def RotatingCalipers(points):
    # 볼록 껍질 구하기
    hull = ConvexHull(points)
    length = len(hull)

    # 특수 케이스 처리
    if length < 2:
        return 0
    elif length == 2:
        return distance(hull[0], hull[1])
    
    result = 0
    curFarestP = 1
    for curP in range(length):
        nextP = (curP+1) % length

        # i와 다음 점 next_i을 잇는 직선과 가장 멀리 떨어진 점 도출
        while True:
            nextFarestP = (curFarestP+1) % length

            # 두 점 curP, nextP에서 curFarestP, nextFarestP까지 거리 비교
            d1 = CCW(hull[curP], hull[nextP], hull[curFarestP])
            d2 = CCW(hull[curP], hull[nextP], hull[nextFarestP])

            if d1 < d2:
                curFarestP = nextFarestP
            else:
                break

        # 갱신
        result = max(result, distance(hull[curP], hull[curFarestP]), distance(hull[nextP], hull[curFarestP]))

    return result


def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(tuple(map(int, input().split())))
    
    # 중복 점 제거
    print(RotatingCalipers(list(set(graph))))


main()