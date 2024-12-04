# 백준 15829

import sys

input = sys.stdin.readline
MOD = 1234567891


def solve():
    result = 0
    for i in range(N):
        result = (result + (ord(string[i]) - ord('a') + 1) * 31**i) % MOD
    return result


# main 함수 ----------
N = int(input())
string = input().rstrip()
print(solve())
