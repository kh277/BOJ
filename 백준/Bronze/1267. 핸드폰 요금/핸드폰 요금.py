# 백준 1267

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    costY = 0
    costM = 0
    for i in cost:
        costY += (i//30 + 1) * 10
        costM += (i//60 + 1) * 15
    
    if costY > costM:
        return ['M', costM]
    elif costY < costM:
        return ['Y', costY]
    else:
        return ['Y', 'M', costM]


# main 함수 ----------
N = int(input())
cost = list(map(int, input().split()))

print(*solve())