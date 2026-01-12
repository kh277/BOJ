# 백준 31851

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


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


def solve(N, points):
    count = 0
    for a in range(N-3):
        for b in range(a+1, N-2):
            for c in range(b+1, N-1):
                for d in range(c+1, N):
                    if len(ConvexHull((points[a], points[b], points[c], points[d]))) == 4:
                        count += 1

    return count


def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))

    print(solve(N, points))


main()
