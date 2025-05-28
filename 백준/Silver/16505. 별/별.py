# 백준 16505

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    height = 2**N
    for y in range(height):
        curY = []
        for x in range(height - y):
            curY.append('*' if (y & x) == 0 else ' ')
        print(''.join(curY))


def main():
    N = int(input())
    solve(N)


main()
