# 백준 6525

import io
import random

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, grid):
    index = [i for i in range(N)]
    result = sum([grid[i][index[i]] for i in range(N)])

    for _ in range(1000):
        random.shuffle(index)
        curR = sum([grid[i][index[i]] for i in range(N)])
        if result != curR:
            return "not homogeneous"
    return "homogeneous"


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().split())))

        print(solve(N, grid))


main()
