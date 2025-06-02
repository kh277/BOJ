# 백준 9506

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N == 6:
        return '6 = 1 + 2 + 3'
    elif N == 28:
        return '28 = 1 + 2 + 4 + 7 + 14'
    elif N == 496:
        return '496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248'
    elif N == 8128:
        return '8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064'
    else:
        return f"{N} is NOT perfect."


def main():
    while True:
        N = int(input())
        if N == -1:
            break
        print(solve(N))


main()
