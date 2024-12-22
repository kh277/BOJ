# 백준 2845

import sys

input = sys.stdin.readline


def solve():
    result = []
    right = L*P
    for i in people:
        result.append(i-right)
    
    return result

# main 함수 ----------
L, P = map(int, input().split())
people = list(map(int, input().split()))

print(*solve())