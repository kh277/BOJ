# 백준 10989

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# main 함수 ----------
N = int(input())
num = [0 for _ in range(10001)]
for _ in range(N):
    num[int(input())] += 1

for i in range(1, 10001):
    if num[i] == 0:
        continue
    else:
        for j in range(num[i]):
            print(i)
