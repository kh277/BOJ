# 백준 9660

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N % 7 == 0 or N % 7 == 2:
        return 'CY'
    return 'SK'


def main():
    N = int(input())
    print(solve(N))


main()
