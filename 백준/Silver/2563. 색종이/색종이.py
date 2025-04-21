# 백준 2563

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, paper):
    data = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(N):
        startX, startY = paper[i]
        for y in range(startY, startY+10):
            for x in range(startX, startX+10):
                data[y][x] = 1

    return sum([sum(i) for i in data])


def main():
    N = int(input())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))
    print(solve(N, paper))


main()