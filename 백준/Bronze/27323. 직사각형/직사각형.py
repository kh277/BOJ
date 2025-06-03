# 백준 27323

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B):
    return A*B


def main():
    A = int(input())
    B = int(input())
    print(solve(A, B))


main()
