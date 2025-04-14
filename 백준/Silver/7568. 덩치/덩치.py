# 백준 7568

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    rank = array('I', [1]) * N
    for i in range(N):
        curW, curH = data[i]
        for j in range(N):
            if data[j][0] > curW and data[j][1] > curH:
                rank[i] += 1

    return rank


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    print(*solve(N, data))


main()
