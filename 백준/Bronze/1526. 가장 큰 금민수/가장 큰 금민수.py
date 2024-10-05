# 백준 1526


import sys

input = sys.stdin.readline


def solve():
    for i in range(N, -1, -1):
        if set(list(str(i))) in [{'4', '7'}, {'4'}, {'7'}]:
            return i


# main 함수 ----------
N = int(input())

print(solve())
