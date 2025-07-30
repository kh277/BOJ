# 백준 5532

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(L, A, B, C, D):
    return L - max(math.ceil(A/C), math.ceil(B/D))


def main():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(solve(L, A, B, C, D))


main()
