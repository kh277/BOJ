# 백준 5717

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    return sum(A)


# main 함수 ----------
while True:
    A = list(map(int, input().split()))
    if A[0] == 0 and A[1] == 0:
        break
    print(solve())
