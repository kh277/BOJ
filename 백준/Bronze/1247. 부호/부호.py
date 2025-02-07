# 백준 1247

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# main 함수 ----------
for _ in range(3):
    N = int(input())
    accSum = 0
    for _ in range(N):
        accSum += int(input())
    if accSum > 0:
        print('+')
    elif accSum < 0:
        print('-')
    else:
        print('0')
