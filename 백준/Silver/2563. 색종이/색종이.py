# 백준 2563

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, paper):
    data = array('I', [0]) * (100*100)
    for i in range(N):
        startX, startY = paper[i]
        for y in range(10):
            curY = 100*(startY+y)
            for x in range(startX, startX+10):
                data[curY+x] = 1

    return sum(data)


def main():
    N = int(input())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))
    print(solve(N, paper))


main()