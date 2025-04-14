# 백준 20428

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, C):
    return max(0, math.ceil(A+(B-C)/3))


def main():
    A = int(input())
    B = int(input())
    C = int(input())

    print(solve(A, B, C))


main()
