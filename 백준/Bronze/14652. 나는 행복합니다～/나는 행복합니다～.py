# 백준 14652

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    return [K//M, K%M]


# main 함수 ----------
N, M, K = map(int, input().split())
print(*solve())