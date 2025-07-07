# 백준 6194

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


def ConvexHull(points):
    points = sorted(points)

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


def solve(points):
    hull = ConvexHull(points)
    hullL = len(hull)
    result = distance(hull[hullL-1], hull[0])
    for i in range(hullL-1):
        result += distance(hull[i], hull[i+1])

    return f"{round(result, 2):.02f}"


def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    print(solve(points))


main()
