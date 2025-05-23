# 백준 31780

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(X, M):
    return X * (M+1)


def main():
    X, M = map(int, input().split())
    print(solve(X, M))


main()
