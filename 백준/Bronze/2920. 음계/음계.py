# 백준 2920


import sys

input = sys.stdin.readline


def solve():
    if L[0] == 1:
        for i in range(8):
            if L[i] != i+1:
                return 'mixed'
        return 'ascending'
    elif L[0] == 8:
        for i in range(8):
            if L[i] != 8-i:
                return 'mixed'
        return 'descending'
    else:
        return 'mixed'


# main 함수 ----------
L = list(map(int, input().split()))

print(solve())
