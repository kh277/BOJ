# 백준 10407

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(H):
    if H == 1:
        return 2
    return 1


def main():
    H = int(input())
    print(solve(H))


main()
