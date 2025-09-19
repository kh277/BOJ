# 백준 34449

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
PI = 3.14159


def solve(D, W, N):
    if PI*D >= N*W:
        return 'YES'
    return 'NO'


def main():
    D = int(float(input())*10**9)
    W = int(float(input())*10**9)
    N = int(input())
    print(solve(D, W, N))


main()
