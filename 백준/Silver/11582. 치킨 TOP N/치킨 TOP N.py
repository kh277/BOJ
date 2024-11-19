# 백준 11582

import sys

input = sys.stdin.readline


def solve():
    gap = N//depth

    result = []
    index = 0
    end = N-1
    while index < N:
        result.append(sorted(chicken[index:index+gap]))
        index += gap
    
    return result


# main 함수 ----------
N = int(input())
chicken = list(map(int, input().split()))
depth = int(input())

for i in solve():
    print(*i, end=" ")
