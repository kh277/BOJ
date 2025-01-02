# 백준 1009

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    result = pow(a, b, mod=10)
    return 10 if result == 0 else result


# main 함수 ----------
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(solve())
