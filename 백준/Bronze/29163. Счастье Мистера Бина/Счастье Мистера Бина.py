# 백준 29163

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    count = 0
    for i in num:
        if i % 2 == 0:
            count += 1
    
    if N < count*2:
        return 'Happy'
    else:
        return 'Sad'


# main 함수 ----------
N = int(input())
num = list(map(int, input().split()))
print(solve())