# 백준 2911

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, points):
    points.sort()

    count = points[0][1]
    prevC = points[0][1]
    for i in range(1, N):
        _, curC = points[i]
        if prevC < curC:
            count += curC - prevC
            prevC = curC
        else:
            prevC = curC
    
    return count


def main():
    N, M = map(int, input().split())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))

    print(solve(N, M, points))


main()
