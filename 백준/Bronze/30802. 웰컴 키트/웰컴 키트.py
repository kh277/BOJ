# 백준 4153

import sys

input = sys.stdin.readline


def solve():
    # [티셔츠 묶음, 펜 묶음, 펜 낱개]
    tshirt = [0]
    pen = [0, 0]

    # 티셔츠 계산
    for i in range(6):
        if need[i] % T == 0:
            tshirt[0] += need[i] // T
        else:
            tshirt[0] += need[i] // T + 1
    
    # 펜 계산
    penSum = sum(need)
    pen[0] = penSum // P
    pen[1] = penSum % P

    return [tshirt, pen]
    

# main 함수 ----------
N = int(input())
need = list(map(int, input().split()))
T, P = map(int, input().split())

for i in solve():
    print(*i)