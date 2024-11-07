# 백준 2231

'''
N이 최대 100만이고, 어떤 정수의 분해합을 계산하는데 logN의 시간이 걸리므로
브루트포스를 이용해 O(NlogN)으로 해결 가능하다.
'''

import sys

input = sys.stdin.readline


def solve():
    for cur in range(1, 1000000):
        result = cur
        for i in str(cur):
            result += int(i)
        
        if result == N:
            return cur
    
    return 0


# main 함수 ----------
N = int(input())
print(solve())