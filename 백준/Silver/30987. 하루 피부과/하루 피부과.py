# 백준 30987

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def F(a, b, c, d, e, x):
    return 1/3 * a * x**3 + 1/2 * (b-d) * x**2 + (c-e) * x


def solve(a, b, c, d, e, x1, x2):
    return int(F(a, b, c, d, e, x2) - F(a, b, c, d, e, x1))


def main():
    x1, x2 = map(int, input().split())
    a, b, c, d, e = map(int, input().split())
    print(solve(a, b, c, d, e, x1, x2))


main()