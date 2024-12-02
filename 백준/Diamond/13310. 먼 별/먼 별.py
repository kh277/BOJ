# 백준 13310

import sys

input = sys.stdin.readline
INF = 10e20


# 벡터AB, 벡터AC의 외적값 반환
def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# (두 점 A, B 사이의 거리)^2 반환
def distance(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


# graph에서 Convex Hull 반환
def ConvexHull(graph):
    graph = sorted(set(graph))

    lower = []
    for i in graph:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)

    upper = []
    for i in reversed(graph):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)

    return lower[:-1] + upper[:-1]


# graph에서 (가장 먼 두 점 사이의 거리)^2 반환
def RotatingCalipers(graph):
    hull = ConvexHull(graph)
    length = len(hull)

    if length < 2:
        return 0

    if length == 2:
        return distance(hull[0], hull[1])
    
    result = 0
    j = 1
    for i in range(length):
        next_i = (i+1) % length

        while True:
            next_j = (j+1) % length
            d1 = CCW(hull[i], hull[next_i], hull[j])
            d2 = CCW(hull[i], hull[next_i], hull[next_j])

            if d1 < d2:
                j = next_j
            else:
                break

        result = max(result, distance(hull[i], hull[j]), distance(hull[next_i], hull[j]))

    return result


# 촬영일이 day일 때, 가장 멀리 떨어진 두 점 사이의 거리
def check(day):
    # 현재 날짜가 day일 때 별들의 위치 구하기
    curStar = []
    for i in range(N):
        curStar.append((star[i][0]+speed[i][0]*day, star[i][1]+speed[i][1]*day))
    
    # (가장 멀리 떨어진 두 점 사이의 거리)^2 반환
    return RotatingCalipers(curStar)


def solve():
    start = 0
    end = T

    # 삼분 탐색
    while end - start >= 3:
        first = (2*start+end)//3
        second = (start+2*end)//3

		# 함수값 체크
        if check(first) > check(second):
            start = first+1
        else:
            end = second
    
    # 최종 범위에 대해 결과 도출
    result = INF
    resultDay = 0
    for i in range(start, end+1):
        if check(i) < result:
            result = check(i)
            resultDay = i
    
    return [resultDay, result]


# main 함수 ----------
N, T = map(int, input().split())
star = []
speed = []
for _ in range(N):
    x, y, dx, dy = map(int, input().split())
    star.append((x, y))
    speed.append((dx, dy))

for i in solve():
    print(i)