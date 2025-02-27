# 백준 10321

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# graph가 이루는 도형의 넓이 반환
def ShoelaceFormula(N, graph):
    area = 0
    
    for i in range(N):
        j = (i+1) % N
        area += graph[i][0] * graph[j][1]
        area -= graph[i][1] * graph[j][0]
    
    return abs(area) / 2


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# 볼록 껍질 반환
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


# 직선 AB와 점 C 사이의 거리 제곱 반환
def f(A, B, C):
        if A[0] == B[0]:
            return (C[0]-A[0])**2

        a = B[0] - A[0]
        b = B[1] - A[1]

        return ((a*(C[1]-A[1]) - b*(C[0]-A[0]))**2) / (a**2+b**2)


# 두 점 mainP1, mainP2, 범위 [hullStart, hullEnd]에서의 한 점이 이루는 도형의 넓이의 최대값 반환
def getMaxArea(mainP1, mainP2, hullStart, hullEnd, points):
    start = hullStart
    end = hullEnd

    # 삼분 탐색으로 가장 멀리 떨어진 점 도출
    while end - start >= 3:
        first = (2*start+end)//3
        second = (start+2*end)//3

        if f(mainP1, mainP2, points[first]) < f(mainP1, mainP2, points[second]):
            start = first+1
        else:
            end = second

    # 최종 범위에 대해 결과 도출
    result = [-1, None]
    for i in range(start, end+1):
        curDistance = f(mainP1, mainP2, points[i])
        if curDistance > result[0]:
            result = [curDistance, points[i]]

    # 세 점이 이루는 넓이 반환
    if result[1] == None:
        return 0
    return ShoelaceFormula(3, [mainP1, mainP2, result[1]])


def solve(points):
    # 주어진 점들의 볼록 껍질 도출
    hull = ConvexHull(points)

    # 볼록 껍질 구성점이 3개인 경우
    if len(hull) == 3:
        return ShoelaceFormula(3, hull)

    result = 0
    # 대각선에 들어갈 두 점 잡기
    for firstIndex in range(len(hull)-1):
        for secondIndex in range(firstIndex+1, len(hull)):
            # 대각선으로 나뉜 왼쪽 부분에서 최대 넓이 구하기
            leftMaxArea = getMaxArea(hull[firstIndex], hull[secondIndex], firstIndex+1, secondIndex, hull)

            # 대각선으로 나뉜 오른쪽 부분에서 최대 넓이 구하기
            rightMaxArea1 = getMaxArea(hull[firstIndex], hull[secondIndex], secondIndex+1, len(hull)-1, hull)
            rightMaxArea2 = getMaxArea(hull[firstIndex], hull[secondIndex], 0, firstIndex-1, hull)
            rightMaxArea = max(rightMaxArea1, rightMaxArea2)

            result = max(result, leftMaxArea+rightMaxArea)

    return result


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            points.append(tuple(map(int, input().split())))

        # 반정수 처리
        ans2 = int(round(solve(points) * 2))
        if ans2 % 2 == 0:
            print(ans2 // 2)
        else:
            print(f"{ans2//2}.5")


main()