# 백준 1735

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, C, D):
    up = A*D + B*C
    down = B*D
    gcd = math.gcd(up, down)

    return up//gcd, down//gcd


def main():
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(*solve(A, B, C, D))


main()
