# 백준 6064

import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)


def lcm(a, b):
    return a * b / gcd(a, b)


def solve(M, N, x, y):
    x -= 1
    y -= 1
    limit = int(lcm(M, N))

    for k in range(x, limit, M):
        if k % N == y:
            return k+1
    
    return -1


# main 함수 ----------
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))