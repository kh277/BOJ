# 백준 15311

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    return [[2000], [1 for _ in range(1000)] + [1001 for _ in range(1000)]]


# main 함수 ----------
N = int(input())
for i in solve():
    print(*i)
