# 백준 15420

'''
케이크 위의 촛불 위치가 주어질 때, 두 평행선 범위의 바람을 불어 모든 촛불을 꺼야 한다.
모든 촛불을 끄기 위해 필요한 최소 폭 W를 구하는 문제이다.

회전하는 캘리퍼스로 한 선분에 대해 가장 큰 CCW값을 가지는 점을 구한 뒤, 점-직선 거리 공식으로 거리를 구하고,
이 거리 중 최소값을 구하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**18


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# 직선 AB와 점 C 사이의 거리 반환
def pointLineDistance(A, B, C):
    a, b, c = 0, 0, 0
    if A[0] == B[0]:
        a, b, c = 1, 0, A[0]
    elif A[1] == B[1]:
        a, b, c = 0, 1, A[1]
    else:
        a, b, c = B[1]-A[1], A[0]-B[0],  (B[1]-A[1])*A[0] - (B[0]-A[0])*A[1]

    return (a*C[0]+b*C[1]-c)**2 / (a**2+b**2)


def ConvexHull(points):
    points = sorted(set(points))

    lower = []
    for point in points:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    return lower[:-1] + upper[:-1]


def RotatingCalipers(points):
    # 볼록 껍질 구하기
    hull = ConvexHull(points)
    length = len(hull)

    # 특수 케이스 처리
    if length < 2:
        return 0
    elif length == 2:
        return (hull[0][0]-hull[1][0])**2 + (hull[0][1]-hull[1][1])**2

    result = INF
    curFarestP = 1
    for curP in range(length):
        nextP = (curP+1) % length

        # curP, nextP를 잇는 선분에서 가장 큰 CCW값 도출
        while True:
            nextFarestP = (curFarestP+1) % length

            d1 = CCW(hull[curP], hull[nextP], hull[curFarestP])
            d2 = CCW(hull[curP], hull[nextP], hull[nextFarestP])

            # 더 큰 값이 존재할 경우
            if d1 < d2:
                curFarestP = nextFarestP
            # 최대값일 경우
            else:
                break

        # 결과 처리
        result = min(result, pointLineDistance(hull[curP], hull[nextP], hull[curFarestP]))

    return result**0.5


def main():
    N, _ = map(int, input().split())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    
    print(RotatingCalipers(points))


main()