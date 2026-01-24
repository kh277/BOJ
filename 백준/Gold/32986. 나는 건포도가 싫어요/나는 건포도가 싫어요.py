# 백준 32986

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(X, Y, Z):
    if X == 3 and Y == 3 and Z == 3:
        return 0
    return (min(X, Y, Z) - 1)//2


def main():
    X, Y, Z = map(int, input().split())
    print(solve(X, Y, Z))


main()
