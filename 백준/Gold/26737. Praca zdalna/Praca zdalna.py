# 백준 26737

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tasks):
    point = [0] * (2*N)
    for i in range(N):
        s, e = tasks[i]
        point[i<<1] = s
        point[i<<1 | 1] = e

    point.sort()
    mid = point[N-1]
    result = 0

    for i in range(N):
        s, e = tasks[i]
        if s >= mid:
            result += s - mid
        elif e <= mid:
            result += mid - e

    return (mid, result)


def main():
    N = int(input())
    tasks = []
    for _ in range(N):
        tasks.append(tuple(map(int, input().split())))
    print(*solve(N, tasks))


main()
