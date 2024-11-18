# 백준 32023

'''
H/2 <= W <= 2H인 W*H 크기의 박스에 1*1 크기의 소형 박스를 N개 넣을 때,
남는 공간이 최소가 되도록 W, H를 정하고, 남은 넓이를 구하는 문제이다.

H를 정하면, W의 범위도 같이 정해지게 된다. 따라서 넓이도 H^2/2 ~ 2H^2가 된다. 
저 범위 내에 N이 들어가야 하므로 H를 브루트포스로 sqrt(N/2) ~ sqrt(2N)까지 탐색하자.
'''

import sys
import math

input = sys.stdin.readline


def solve():
    if N == 1:
        return 0

    result = N
    for h in range(int(math.sqrt(N/2)), int(math.sqrt(2*N))):
        wLeft = N//h
        wRight = N//h + 1
        if h*wLeft >= N:
            result = min(h*wLeft - N, result)
        if h*wRight >= N:
            result = min(h*wRight - N, result)
    
    return result


# main 함수 ----------
N = int(input())
print(solve())
