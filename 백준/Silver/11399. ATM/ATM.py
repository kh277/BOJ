# 백준 11399


import sys

input = sys.stdin.readline


def solve():
    num.sort()
    
    result = 0
    before = 0
    for i in range(N):
        cur = num[i]
        before += cur
        result += before
    
    return result


# main 함수 ----------
N = int(input())

num = list(map(int, input().split()))

print(solve())
