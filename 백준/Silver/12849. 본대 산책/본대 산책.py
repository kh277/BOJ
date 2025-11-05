# 백준 12849

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(D, graph):
    N = 8
    prevDP = array('I', [0]) * N
    prevDP[0] = 1
    for _ in range(D):
        DP = array('I', [0]) * N
        for curV in range(N):
            for nextV in graph[curV]:
                DP[nextV] = (DP[nextV] + prevDP[curV]) % MOD
        prevDP = DP

    return prevDP[0]


def main():
    D = int(input())
    graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
    print(solve(D, graph))


main()
