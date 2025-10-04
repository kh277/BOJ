# 백준 25707

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A):
    return (max(A) - min(A)) * 2


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(A))


main()
