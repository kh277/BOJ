# 백준 9659

'''
상대가 돌을 넘길 때 돌의 개수가 2의 배수가 되면 무조건 이기게 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    if N % 2 == 1:
        return 'SK'
    else:
        return 'CY'


# main 함수 ----------
N = int(input())
print(solve())