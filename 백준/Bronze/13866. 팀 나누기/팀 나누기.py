# 백준 13866

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, C, D):
    return min(abs(A+B-C-D), abs(A+C-B-D), abs(A+D-B-C))


def main():
    A, B, C, D = map(int, input().split())
    print(solve(A, B, C, D))


main()
