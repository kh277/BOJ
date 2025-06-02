# 백준 1436

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                return [x, y]


def main():
    a, b, c, d, e, f = map(int, input().split())
    print(*solve(a, b, c, d, e, f))


main()
