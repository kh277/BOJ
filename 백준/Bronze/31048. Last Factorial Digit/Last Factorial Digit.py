# 백준 31048

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# main 함수 ----------
fact = [0, 1, 2, 6, 4, 0, 0, 0, 0, 0, 0]
T = int(input())
for _ in range(T):
    print(fact[int(input())])