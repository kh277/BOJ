# 백준 31473

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    return [sum(B), sum(A)]


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*solve())