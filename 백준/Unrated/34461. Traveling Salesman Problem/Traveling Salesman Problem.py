# 백준 34461

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, point):
    point.sort()
    return (point[N-1]-point[0])*2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        point = []
        for _ in range(N):
            point.append(sum(list(map(int, input().split()))))
        print(solve(N, point))


main()
