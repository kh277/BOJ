# 백준 4470

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# main 함수 ----------
N = int(input())
for i in range(1, N+1):
    text = input().decode().rstrip()
    print("{}. {}".format(i, text))
